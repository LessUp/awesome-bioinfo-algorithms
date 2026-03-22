"""
Shared pytest fixtures for awesome-bioinfo-algorithms tests.
"""
import os

import pytest

from scripts.algorithm_registry import AlgorithmRegistry
from scripts.category_manager import CategoryManager
from scripts.schema import AlgorithmEntry, Category


@pytest.fixture
def project_root():
    """Return the project root directory."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture
def data_dir(project_root):
    """Return the data directory path."""
    return os.path.join(project_root, 'data')


@pytest.fixture
def sample_category():
    """Create a sample category for testing."""
    return Category(
        id='sequence-alignment',
        name='序列比对',
        name_en='Sequence Alignment',
        description='用于比较和对齐生物序列的算法',
        subcategories=[
            Category(
                id='pairwise',
                name='双序列比对',
                name_en='Pairwise Alignment',
                description='两条序列之间的比对算法',
                subcategories=[],
                parent_id='sequence-alignment'
            )
        ],
        parent_id=None
    )


@pytest.fixture
def sample_algorithm():
    """Create a sample algorithm entry for testing."""
    return AlgorithmEntry(
        id='smith-waterman',
        name='Smith-Waterman',
        description='经典的局部序列比对算法，使用动态规划方法找出两条序列之间相似性最高的局部区域。'
                    '该算法保证找到最优的局部比对结果，适用于检测序列中的保守区域和功能域。',
        purpose='局部序列比对，寻找序列间的相似区域',
        time_complexity='O(mn)',
        category='sequence-alignment',
        space_complexity='O(mn)',
        year=1981,
        paper_url='https://doi.org/10.1016/0022-2836(81)90087-5',
        implementation_url='https://github.com/mengyao/Complete-Striped-Smith-Waterman-Library',
        related_tools=['BLAST', 'FASTA', 'SSEARCH'],
        tags=['dynamic-programming', 'local-alignment', 'classic'],
        subcategory='pairwise',
    )


@pytest.fixture
def loaded_registry(data_dir):
    """Create a registry loaded with real project data."""
    algorithms_dir = os.path.join(data_dir, 'algorithms')
    registry = AlgorithmRegistry(algorithms_dir)
    registry.load_all()
    return registry


@pytest.fixture
def loaded_category_manager(data_dir):
    """Create a category manager loaded with real project data."""
    categories_path = os.path.join(data_dir, 'categories.yaml')
    manager = CategoryManager()
    manager.load_categories(categories_path)
    return manager
