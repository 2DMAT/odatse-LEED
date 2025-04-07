#!/bin/sh

export PYTHONUNBUFFERED=1
export OMPI_MCA_rmaps_base_oversubscribe=true


# Clean up output directory by running prepare.sh
sh ./prepare.sh

# Run the LEED optimization in parallel using MPI with 4 processes
# Takes input parameters from input.toml file and measures execution time
time mpiexec -np 4 odatse-LEED input.toml

# Define paths for result and reference files
result=output/ColorMap.txt    # Output file containing color map data
reference=ref_ColorMap.txt    # Reference file with expected color map

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
