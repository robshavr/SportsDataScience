<h1> Overview: vlmax.py</h1>
<h2> import local file</h2>
To import the local file:<br>
<code>from vlamax.py import Model</code>

<h2> "Model" Class overview</h2>
Create the class: <code>Test = Model(VO2max=60)</code>

<h3> Parameters</h3>

following parameters are given for creating the Model. If none are given, then the defualt values will be used:
- VO2max = 58.6
- vLamax = 0.5
- RunningEco = 11.95
- Ks1 = 0.25
- Ks2 = 1.2
- VolRel = 0.45

After creating the model, following values will be calculated and can be retrieved:
- ADP
- vLass
- LaComb
- vLanet

<h3> functions</h3>
<h4> update(VO2max, vLamax, RunningEco, Ks1, Ks2, VolRel)</h4>
<code>Test.update(VO2max = 58.6,       
    vLamax = 0.5,      
    RunningEco = 11.95,
    Ks1 = 0.25,     
    Ks2 = 1.2,    
    VolRel = 0.45)</code>
The update function takes in the same parameters like the constructor and calculate the values again. It is later used for the slider.
The default values are just like in the constructor. If the update() function is used, it is better to input all parameters, if not the default value will be used.

<h4> recalculate()</h4>
It is recommended to change a value in the class and use the function <code>recalculate()</code>. This function calculates the ADP, vLass, LaComb and vLanet again. <br>
<code>Test.VO2max = 57.5</code><br>
<code>Test.recalculate()</code>

<h4>plot_lactate()</h4>
<code>Test.plot_lactate()</code>
This function plots the current values.

<h4>slider()</h4>
<code>Test.slider()</code> This function only works for Jupyter notebook now</code>



