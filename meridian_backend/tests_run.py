import pytest
import sys

if __name__ == "__main__":
    ret = pytest.main(["tests/", "-q", "--tb=short"])
    sys.exit(ret)
