Analyses by user programs
================================================================

In this tutorial, we will write a user program using odatse-LEED module and perform analyese. As an example, we adopt Nelder-Mead method for the inverse problem algorithm.


Location of the sample files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sample files are located in ``sample/user_program``.
The following files are stored in the folder.

- ``simple.py``

  Source file of the main program. This program reads ``input.toml`` for the parameters.

- ``input.toml``

  Input file of the main program.

- ``base``

  Directory that contains reference files to proceed with calculations in the main program.
  The reference files include: ``exp.d``, ``rfac.d``, ``tleed4.i``, and ``tleed5.i``.

- ``ref.txt``

  A reference file for the result of the calculation.

- ``prepare.sh`` , ``do.sh``

  Script prepared for doing all calculation of this tutorial

The following sections describe these files and then show the actual calculation results.


Description of main program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``simple.py`` is a simple program for the analyses using odatse-LEED module.
The entire source file is shown as follows:

.. code-block:: python

    import odatse
    import odatse.algorithm.min_search
    from odatse.extra.LEED import Solver
    
    info = odatse.Info.from_file("input.toml")
    
    solver = Solver(info)
    runner = odatse.Runner(solver, info)
    alg = odatse.algorithm.min_search.Algorithm(info, runner)
    alg.main()


At the beginning of the program, the required modules are imported as listed below.

- ``odatse`` for the main module of ODAT-SE.

- ``odatse.algorithm.min_search`` for the module of the inverse problem algorithm used in this tutorial.

- ``odatse.extra.LEED`` for the direct problem solver module.

Next, the instances of the classes are created.

- ``odatse.Info`` class

  This class is for storing the parameters. It is created by calling a class method ``from_file`` with a path to TOML file as an argument.

- ``odatse.extra.LEED.Solver`` class

  This class is for the direct problem solver of the odatse-LEED module. It is created by passing an instance of Info class.

- ``odatse.Runner`` class

  This class is for connecting the direct problem solver and the inverse problem algorithm. It is created by passing an instance of Solver class and an instance of Info class.

- ``odatse.algorithm.min_search.Algorithm`` class

  This class is for the inverse problem algorithm. In this tutorial, we use ``min_search`` module that implements the optimization by Nelder-Mead method. It is created by passing an instance of Runner class.

After creating the instances of Solver, Runner, and Algorithm in this order, we invoke ``main()`` method of the Algorithm class to start analyses.

In the above program, the input parameters are read from a file in TOML format. It is also possible to take the parameters in the form of dictionary.


Input files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The input file for the main program, ``input.toml``, contains parameters for the direct problem solver and the inverse problem algorithm. The contents of the ``base`` and ``solver`` sections are the same as those in the previous example.

The parameters for the Nelder-Mead method should be specified in the ``algorithm.param`` section, while ``algorithm.name`` for the type of algorithm is ignored.

- ``min_list`` and ``max_list`` specifies the search region in the form of the lower and upper bounds of the parameters as lists.

- ``initial_list`` and ``initial_scale_list`` specify the initial simplex. For the two-parameter case, when ``initial_list = [z1, z2]`` and ``initial_scale_list = [dz1, dz2]`` are specified, a triangle is taken as an initial simplex that has the vertices at ``[z1, z2]``, ``[z1+dz1, z2]``, and ``[z1, z2+dz2]``.


Calculation execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before running the sample program, you need to run ``setup.sh`` in the ``sample/satleed`` directory to compile SATLEED and generate ``satl1.exe`` and ``satl2.exe``.

Move to the directory in which sample files are located:

.. code-block::

   $ cd sample/user_program

Then, run the main program. The computation time will take only a few minutes on a normal PC.

.. code-block::

   $ python3 simple.py | tee log.txt

The standard output will be shown like as follows.

.. code-block::

    label_list      : ['z1', 'z2']
    param.min_list  : [-0.5, 0.75]
    param.max_list  : [0.5, 2.75]
    param.initial_list: [-0.2, 1.75]
    minimize.initial_scale_list: [0.02, 0.02]
    eval: x=[-0.18  1.75], fun=0.9422
    eval: x=[-0.14  1.72], fun=0.8607
    eval: x=[-0.12  1.745], fun=0.7262
    eval: x=[-0.03  1.6975], fun=0.4055
    eval: x=[-0.01  1.7225], fun=0.3186
    eval: x=[-0.01  1.7225], fun=0.3186
    eval: x=[-0.045 1.71875], fun=0.2953
    eval: x=[-0.025 1.74375], fun=0.2157
    ...


``z1`` and ``z2`` are the candidate parameters at each step, and ``R-factor`` is the function value at that point.
The final estimated parameters will be written to ``output/res.dat``. 
In the current case, the following result will be obtained:

.. code-block::

    fx = 0.2101
    z1 = -0.01991012930870084
    z2 = 1.7509844067692764
        
You can see that we will get the same values as the correct answer data in ``ref.txt``.

Note that ``do.sh`` is available as a script for batch calculation.

