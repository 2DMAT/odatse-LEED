#!/bin/sh

export PYTHONUNBUFFERED=1
export OMPI_MCA_rmaps_base_oversubscribe=true


# Clean up output directory by running prepare.sh
sh ./prepare.sh

# Run the optimization script and measure execution time
# Using simple.py which reads config from input.toml
time python3 ./simple.py

# Define paths for result and reference files
result=output/res.txt    # Output file containing optimization results
reference=ref.txt        # Reference file with expected results

# Compare result against reference using diff
echo diff $result $reference
res=0
#diff $result $reference || res=$?
python3 ../tools/almost_diff.py $result $reference || res=$?

# Check if files match and report test status
if [ $res -eq 0 ]; then
  # Files are identical - test passed
  echo TEST PASS
  true
else
  # Files differ - test failed
  echo TEST FAILED: $result and $reference differ
  false
fi
