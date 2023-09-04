# Fabric Data Analysis
This is a class project for Fudan COMP130030.01 Pattern Recogniztion class. 

## Project Descripition
A flaw in fabric can be categrized into 
{
0: 'unknown',
1: 'escape_printing',
2: 'clogging_screen',
3: 'broken_hole',
4: 'toe_closing_defects',
5: 'water_stain',
6: 'smudginess',
7: 'white_stripe',
8: 'hazy_printing',
9: 'billet_defects',
10: 'trachoma',
11: 'color_smear',
12: 'crease',
13: 'false_positive',
14: 'no_alignment'
}.
Given training and testing set of corresponding flaw types, find the best model with highest accuracy.

## Result
During the process of find the best algorithm, we tried out many variations of neural networks. AlexNet turned out to have the most accuracy.
LeNet was the second best algorithm. Being the first major CNN model that used GPU's for training, AlexNet is a deeper architecture with 8
layers and is better at extracting features comparing to LeNet. Other more complicated neural networks, Google net and VGG, turned to
have a lower accuracy, perhaps because the nature of the task is not suitable for them, which means we still require futhur exploration on
what algorithm is most suitable for the task.
1. LeNet-5: 65%
2. Alex Net with BN: 66%
3. Google Net: failed (<40%)
4. VGG: failed (<40%)
