# code-20201128-udhayakumar

# Application | Body-Mass Index (BMI)
	Make program Body-Mass Index (BMI) in Python.

Formula:
```
BMI(kg/m2) = mass(kg) / height(m)2
```

## Table - BMI Category and the Health Risk.
```

BMI Category			BMI Range (kg/m2)	Health risk

Underweight			18.4 and below		Malnutrition risk
Normal weight			18.5 - 24.9	        Low risk
Overweight			25 - 29.9		Enhanced risk
Moderately obese		30 - 34.9		Medium risk
Severely obese			35 - 39.9		High risk
Very severely obese		40 and above		Very high risk

```


## Method-1: Run this Program in Localhost
First, you must install some of library in `requirements.txt` using `python-pip`:
```
pip install -r requirements.txt
```
Then, run:
```
python3 bmi_calculate.py 'filepath'
```
Output:
```
Over All Data
---------------

    Gender  HeightCm  WeightKg  Bmi        Bmi Category       Health Risk
0    Male       175        75   24.49      NormalWeight       Low risk
1    Male       161        85   32.79      Moderately obese   Medium risk
2    Male       180        77   23.77      NormalWeight       Low risk
3  Female       166        62   22.50      NormalWeight       Low risk
4  Female       150        70   31.11      Moderately obese   Medium risk
5  Female       167        82   29.40      Overweight         Enhanced risk

Statistics
--------------
NormalWeight        3
Moderately obese    2
Overweight          1


```
