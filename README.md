# Modelling experimental pendulum data using Python

The purpose of this project was to analyse experimental data for two pendulums of different masses to extract a value of g. 

- Two datasets, with data for pendulum length and period of oscillation, are read in with pandas
- These are analysed with least squares methods to fit parameters to the straight-line equation:
    T^2 = g / L
- This is then visualised with matplotlib, and the values for g are presented
- Uncertainties from the experiment are analysed and presented as well for context.

  <img width="851" height="545" alt="pendulum-1" src="https://github.com/user-attachments/assets/5f9d3312-cb4e-4884-9a99-038f904c7ac0" />
<img width="865" height="545" alt="pendulum-2" src="https://github.com/user-attachments/assets/bb1f70a4-2b3d-46e4-b195-3cc3c9a97357" />
