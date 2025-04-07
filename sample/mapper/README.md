# Simple example of odatse-LEED

## What's this

This example demonstrates LEED (Low Energy Electron Diffraction) analysis of a clean Cu(001) surface. LEED is a surface science technique used to determine the atomic structure of crystal surfaces. The experimental I-V curves used here are taken from Figure 1 of the reference paper cited below. 

[1] Md Kabiruzzaman, Rezwan Ahmed, Takeshi Nakagawa, and Seigi Mizuno,
Investigation of c(2×2) Phase of Pb and Bi Coadsorption on Cu(001) by Low Energy Electron Diffraction, Evergreen. 4 (1), pp. 10-15 (2017) https://doi.org/10.5109/1808306

## Files

### Key files in this example:

- `README.md`
    - this file containing documentation and instructions
- `do.sh`
    - Main execution script that runs the py2dmat optimization framework
- `input.toml`
    - Configuration file for py2dmat defining the optimization problem
- `MeshData.txt`
    - Contains the grid points in parameter space to be explored

### setup files for SATLEED in ../satleed directory
- `setup.sh`
    - Shell script to prepare the SATLEED environment:
        - Downloads and extracts SATLEED package
        - Modifies configuration parameters
        - Creates build system files
        - Compiles the executables
- `leedsatl.patch`
- `leedsatl_arraysize.patch`
- `leedsatl_pause.patch`
    - Patch files containing parameter and other modifications for SATLEED

## Flow

Step 1: Build the SATLEED executables

  This compiles satl1.exe and satl2.exe which perform the LEED calculations

  ``` bash
  sh ./setup.sh
  ```

Step 2: Perform grid search

  This runs the py2dmat optimization framework to find the optimal parameters

  ``` bash
  sh ./do.sh
  ```
