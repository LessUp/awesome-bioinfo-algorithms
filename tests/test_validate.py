"""
Property-based tests for Validator class.
Feature: awesome-bioinfo-algorithms
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hypothesis import given, settings, strategies as st, assume, HealthCheck
from scripts.validate import Validator, ValidationResult


# Strategies for generating test data
valid_id = st.text(
    alphabet=st.sampled_from('abcdefghijklmnopqrstuvwxyz-_0123456789'),
    min_size=1, max_size=50
).filter(lambda x: x and not x.startswith('-'))

valid_name = st.text(min_size=1, max_size=100).filter(lambda x: x.strip())

# Description between 50-200 characters
valid_description = st.text(min_size=50, max_size=200).filter(lambda x: 50 <= len(x.strip()) <= 200)

# Description that's too short
short_description = st.text(min_size=0, max_size=49)

# Description that's too long
long_description = st.text(min_size=201, max_size=300)


@st.composite
def valid_algorithm_data(draw):
    """Generate valid algorithm data dictionary."""
    return {
        'id': draw(valid_id),
        'name': draw(valid_name),
        'description': draw(valid_description),
        'purpose': draw(st.text(min_size=5, max_size=100).filter(lambda x: x.strip())),
        'time_complexity': draw(st.sampled_from(['O(n)', 'O(n^2)', 'O(mn)', 'O(n log n)', 'O(1)'])),
        'category': draw(valid_id),
    }


@st.composite
def algorithm_data_missing_field(draw, field_to_remove: str):
    """Generate algorithm data with a specific required field missing."""
    data = draw(valid_algorithm_data())
    del data[field_to_remove]
    return data


@st.composite
def algorithm_data_empty_field(draw, field_to_empty: str):
    """Generate algorithm data with a specific required field empty."""
    data = draw(valid_algorithm_data())
    data[field_to_empty] = ""
    return data


# Property 3: Required Fields Validation
@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
@given(field_name=st.sampled_from(['id', 'name', 'description', 'purpose', 'time_complexity', 'category']))
def test_property_3_missing_required_field(field_name: str):
    """
    Feature: awesome-bioinfo-algorithms, Property 3: Required Fields Validation
    
    For any algorithm entry submission, if any required field is missing,
    the validator SHALL reject the entry and return an error.
    
    Validates: Requirements 1.4, 2.1, 4.2
    """
    validator = Validator()
    
    # Create valid data then remove the field
    data = {
        'id': 'test-algo',
        'name': 'Test Algorithm',
        'description': 'A' * 60,  # Valid length
        'purpose': 'Testing',
        'time_complexity': 'O(n)',
        'category': 'test-category',
    }
    del data[field_name]
    
    result = validator.validate_algorithm(data)
    
    assert not result.is_valid, f"Should reject when '{field_name}' is missing"
    assert any(field_name in error for error in result.errors), \
        f"Error should mention missing field '{field_name}'"


@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
@given(field_name=st.sampled_from(['id', 'name', 'description', 'purpose', 'time_complexity', 'category']))
def test_property_3_empty_required_field(field_name: str):
    """
    Feature: awesome-bioinfo-algorithms, Property 3: Required Fields Validation
    
    For any algorithm entry submission, if any required field is empty,
    the validator SHALL reject the entry and return an error.
    
    Validates: Requirements 1.4, 2.1, 4.2
    """
    validator = Validator()
    
    # Create valid data then empty the field
    data = {
        'id': 'test-algo',
        'name': 'Test Algorithm',
        'description': 'A' * 60,
        'purpose': 'Testing',
        'time_complexity': 'O(n)',
        'category': 'test-category',
    }
    data[field_name] = ""
    
    result = validator.validate_algorithm(data)
    
    assert not result.is_valid, f"Should reject when '{field_name}' is empty"
    assert any(field_name in error for error in result.errors), \
        f"Error should mention empty field '{field_name}'"


# Property 7: Validation Error Specificity
@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
@given(
    missing_fields=st.lists(
        st.sampled_from(['id', 'name', 'description', 'purpose', 'time_complexity', 'category']),
        min_size=1, max_size=3, unique=True
    )
)
def test_property_7_error_specificity_missing_fields(missing_fields):
    """
    Feature: awesome-bioinfo-algorithms, Property 7: Validation Error Specificity
    
    For any invalid algorithm entry, the validator SHALL return an error message
    that identifies the specific field issue.
    
    Validates: Requirements 4.4, 6.3
    """
    validator = Validator()
    
    # Create data with multiple missing fields
    data = {
        'id': 'test-algo',
        'name': 'Test Algorithm',
        'description': 'A' * 60,
        'purpose': 'Testing',
        'time_complexity': 'O(n)',
        'category': 'test-category',
    }
    for field in missing_fields:
        del data[field]
    
    result = validator.validate_algorithm(data)
    
    assert not result.is_valid
    # Each missing field should be mentioned in errors
    for field in missing_fields:
        assert any(field in error for error in result.errors), \
            f"Error should specifically mention '{field}'"


@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
@given(desc_length=st.integers(min_value=0, max_value=49))
def test_property_7_error_specificity_short_description(desc_length):
    """
    Feature: awesome-bioinfo-algorithms, Property 7: Validation Error Specificity
    
    For description that's too short, the validator SHALL return an error
    that identifies the length issue.
    
    Validates: Requirements 4.4, 6.3
    """
    validator = Validator()
    
    data = {
        'id': 'test-algo',
        'name': 'Test Algorithm',
        'description': 'A' * desc_length,
        'purpose': 'Testing',
        'time_complexity': 'O(n)',
        'category': 'test-category',
    }
    
    result = validator.validate_algorithm(data)
    
    if desc_length < 50:
        assert not result.is_valid
        assert any('short' in error.lower() or 'description' in error.lower() 
                   for error in result.errors), \
            "Error should mention description length issue"


@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
@given(desc_length=st.integers(min_value=201, max_value=300))
def test_property_7_error_specificity_long_description(desc_length):
    """
    Feature: awesome-bioinfo-algorithms, Property 7: Validation Error Specificity
    
    For description that's too long, the validator SHALL return an error
    that identifies the length issue.
    
    Validates: Requirements 4.4, 6.3
    """
    validator = Validator()
    
    data = {
        'id': 'test-algo',
        'name': 'Test Algorithm',
        'description': 'A' * desc_length,
        'purpose': 'Testing',
        'time_complexity': 'O(n)',
        'category': 'test-category',
    }
    
    result = validator.validate_algorithm(data)
    
    assert not result.is_valid
    assert any('long' in error.lower() or 'description' in error.lower() 
               for error in result.errors), \
        "Error should mention description length issue"


# Property 10: Data Format Validation
@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
@given(data=valid_algorithm_data())
def test_property_10_valid_data_passes(data):
    """
    Feature: awesome-bioinfo-algorithms, Property 10: Data Format Validation
    
    For any valid algorithm data, the validator SHALL accept it.
    
    Validates: Requirements 6.2
    """
    validator = Validator()
    result = validator.validate_algorithm(data)
    
    # Valid data should pass (unless description length is wrong)
    desc_len = len(data['description'].strip())
    if 50 <= desc_len <= 200:
        assert result.is_valid, f"Valid data should pass validation. Errors: {result.errors}"


@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
@given(
    tags_value=st.one_of(
        st.text(min_size=1, max_size=20),  # String instead of list
        st.integers(),  # Integer instead of list
        st.dictionaries(st.text(max_size=5), st.text(max_size=5), max_size=2)  # Dict instead of list
    )
)
def test_property_10_invalid_tags_format(tags_value):
    """
    Feature: awesome-bioinfo-algorithms, Property 10: Data Format Validation
    
    For any data with invalid tags format (not a list), the validator SHALL report the violation.
    
    Validates: Requirements 6.2
    """
    validator = Validator()
    
    data = {
        'id': 'test-algo',
        'name': 'Test Algorithm',
        'description': 'A' * 60,
        'purpose': 'Testing',
        'time_complexity': 'O(n)',
        'category': 'test-category',
        'tags': tags_value,
    }
    
    result = validator.validate_algorithm(data)
    
    assert not result.is_valid
    assert any('tags' in error.lower() for error in result.errors), \
        "Error should mention 'tags' field"


# Category validation tests
@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
@given(field_name=st.sampled_from(['id', 'name', 'name_en']))
def test_category_missing_required_field(field_name: str):
    """Test that missing required category fields are detected."""
    validator = Validator()
    
    data = {
        'id': 'test-cat',
        'name': '测试分类',
        'name_en': 'Test Category',
    }
    del data[field_name]
    
    result = validator.validate_category(data)
    
    assert not result.is_valid
    assert any(field_name in error for error in result.errors)
