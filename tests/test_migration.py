import pytest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../src/python"))

from migration_engine import MigrationEngine

class TestMigration:
    @pytest.fixture
    def engine(self):
        # Use a smaller model for tests
        return MigrationEngine(model_name="llama2:7b")
    
    def test_simple_struct_migration(self, engine):
        c_code = """
        typedef struct {
            int x;
            int y;
        } Point;
        
        void move_point(Point *p, int dx, int dy) {
            p->x += dx;
            p->y += dy;
        }
        """
        
        result = engine.migrate(c_code)
        python_code = result["python_code"]
        
        # Basic verification
        assert "class Point" in python_code
        assert "def move_point" in python_code or "def move" in python_code
        assert "self.x" in python_code
        assert "self.y" in python_code
