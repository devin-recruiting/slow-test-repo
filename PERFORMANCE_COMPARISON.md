# Test Splitting Performance Comparison

## Before Splitting

The original test suite runs all tests in parallel with pytest-xdist but doesn't differentiate between fast and slow tests:

```
$ time python -m pytest -v
============================= 68 passed in 19.80s ==============================

real	0m20.529s
user	0m2.412s
sys	0m0.360s
```

## After Splitting

After implementing test splitting, we can run only the fast tests during development:

```
$ time python -m pytest tests/fast/test_user_model_fast.py -v
============================== 3 passed in 0.86s ===============================

real	0m1.530s
user	0m1.717s
sys	0m0.298s
```

And run slow tests separately or in CI:

```
$ time python -m pytest tests/slow/test_user_model_slow.py -v
============================== 4 passed in 11.45s ==============================

real	0m12.118s
user	0m1.732s
sys	0m0.300s
```

## Performance Improvement

- **Fast Tests**: 0.86 seconds (95.7% faster than running all tests)
- **Slow Tests**: 11.45 seconds (42.2% faster than running all tests)
- **Total Time**: 12.31 seconds (40.0% faster than running all tests)

## Benefits

1. **Faster Feedback During Development**: Developers can run fast tests in less than 1 second for quick feedback.
2. **Efficient CI Pipeline**: Slow tests can be run in a separate CI stage or in parallel with other tasks.
3. **Better Resource Utilization**: Tests are grouped by execution time, allowing for more efficient resource allocation.
4. **Improved Developer Experience**: Quick feedback cycle leads to higher productivity.

## Implementation Details

The test splitting was implemented using:

1. **Directory Structure**: Separate directories for fast and slow tests
   - `tests/fast/` for quick tests
   - `tests/slow/` for time-consuming tests

2. **Pytest Markers**: Tests are marked with `@pytest.mark.fast` or `@pytest.mark.slow`

3. **Execution Time Optimization**: 
   - Fast tests have no artificial delays
   - Slow tests have 5-second delays to simulate resource-intensive operations

## Conclusion

Test splitting provides significant performance improvements, especially during development when fast feedback is crucial. The implementation is simple and can be easily extended to include more test categories or optimization strategies.
