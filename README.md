## Docker container for tfcausalimpact

This repository provides a wrapper for the package [WilliamFuks/tfcausalimpact](https://github.com/WillianFuks/tfcausalimpact) - which is itself a python tensorflow implementation of Google's Causal Impact model originally written in R. The only modifications to that package provided here are modifications to the plotting tools that enable them to write to disk directly.

### Inputs and usage

The image can be built directly from the repository using docker build. Currently, all the data pre-processing is handled by hard coded variables (src/consts.py), which require a rebuild to reconfigure them.

The current preprocessing function in utils.py accepts data in a 'long' table, of the form 'Date;Name;Value' that it pivots to wide form - you can supply wide form data if you remove references to make_dataframe.

You must provide a CSV with your raw data in `<path>/input`. 

You can simulate a linear test effect during the test period by setting the variable `test_percent` in `consts.py` to a value greater than 1.

### Outputs

The output is stored in a created folder `<path>/output` that will contain:

* A plot produced by the initial model process completion
* A text file of the summary (containing the posterior probability of an effect)
* Raw data for the components of the plot, for reproducing the plots if that is necessary (to have them match custom reporting themes, or to be included in a plotly artefact)

A sample of the image output is linked below:
![A sample output run on data taken from the Austrian Abwassermonitor datasets in August 2023](https://github.com/fnnsll/causal_impact_docker/blob/main/docs/ci_figure_Wien_Salzburg_04_09_2023_20_48_00.png)

### Next Steps
 
*  Switch from hard coded parameters to either environment variables in docker - or parameters passed by a JSON file - allows configuration without rebuilding
*  Switching to poetry package management for better dependency control
*  Finding a good alternative to bash scripts for model execution - for instance using a make file.
