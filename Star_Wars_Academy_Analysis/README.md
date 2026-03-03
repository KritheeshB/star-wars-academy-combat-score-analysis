# Star Wars Academy Analysis

## Dataset Overview
This project analyzes combat score of academy trainees using basic demographic and force-related attributes.

## How to Run
1. Install required libraries: pandas,matplotlib
2. Ensure 'star_wars_academy.csv' is in the same directory 
3. Run 'Star_Wars_Academy_Code.py'

## Questions to Explore
- Force Sensitivity vs Combat Score
- Midichlorian Count vs Combat Score
- Age vs Combat score
- Planet vs Combat Score
- Lightsaber Colour vs Combat Score
 
### Force Sensitivity vs Combat Score
- With the use of tools such as pandas and python, the average combat score and the median combat score of both force sensitive trainees and non - force sensitive trainees has been found out.
- And using matplotlib, the overall distribution of force sensitive and non force sensitive trainees combat score has been found out.
- Since the dataset is small, bar chart is used to visually compare combat scores across force sensitivity.
- An horizontal bar chart is used to avoid overlapping of long names which makes the chart easier to read. 
- Inferring from these findings the average and median combat scores of force sensitive trainees is higher than that of the non-force sensitive trainees. 
- So from the given dataset, it can be concluded that force sensitive trainees have higher average and median combat scores than non force sensitive trainees.
- However this conclusion might be contradicted considering the fact that the dataset consisted of less force sensitive trainees. 

### Midichlorian Count vs Combat Score
- An attempt to figure out the relationship between midichlorian count and combat score was made using python and pandas quantitatively using the correlation function.
- A manual observation was also made by printing both midichlorian count and combat score and sorting it by midichlorian count in decreasing order.
- To strengthen the observation claim, a scatter plot was plotted between both the desired quantities using matplotlib.
- The dataset shows a moderate positive relationship between midichlorian count and combat score. While higher midichlorian counts tend to be associated with higher combat scores, the relationship is not strong or consistent. 
- If there could be any contradiction for this inference, it could arise considering the validity and the size of the dataset. 

### Age vs Combat Score
- Using python and pandas, an attempt to figure out the relationship between age and combat score has been made quantitatively using the correlation function.
- It was also manually observed by printing both age and combat score and sorting out by age in decreasing order.
- To strengthen the inference made from the observation, a scatter plot was plotted between both the quantities using matplotlib.
- The dataset shows a moderate positive relationship between age and combat score. While older trainees tend to have a higher combat score, the relationship is not strong as some of the younger trainees too have a higher combat score.
- If there could be any contradiction for this inference, it could arise considering the validity and the size of the dataset.

### Planet vs Combat Score
- In an attempt to find the variables on which combat score depends, planet was examined if it's the one being looked for using the groupby function in pandas.  
- The examination process got easier when it was visualised as a bar chart using matplotlib in python.
- It has been inferred that trainees born in planets such as Dagobah, Tatooine and Chandrila have a higher combat score but no real pattern or relationship actually exists between the planet and combat score.   
- This conclusion has a high probability of being false because of the limited size of the dataset. Except Tatooine all other planets mentioned in the dataset have only one trainee which limits the validity of this conclusion on the relationship between planet and combat score.

### Lightsaber Color vs Combat Score
- In an attempt to find the variables on which combat score depends, lightsaber color was examined if it's the one being looked for using the groupby function in pandas.
- The examination process got easier when it was visualised as a bar chart using matplotlib in python.
- It has been inferred that trainees having a lightsaber color of red and green have higher combat scores than the rest.
- This conclusion is highly controversial given the limited size of the dataset.
- Also lightsaber color exists only for force sensitive trainees in the given dataset. So consideration of lightsaber color as a metric for combat score is uncertain.  


## Conclusion:
- Variables such as force sensitivity, midichlorian count, age, planet and lightsaber color were examined to find out if combat score depends on them.
- Analysis on force sensitivity tells than force sensitive trainees have a higher combat score compared to that of non-force sensitive trainees.
- Analysis on midichlorian count and age tells a moderately positive correlation between it and combat score.
- Analysis on planet and lightsaber color tells of no clear relationship between it and combat score.
- Overall it can be said that the probability of trainees to have a high combat score increases with force sensitivity and high midichlorian count. But it doesn't mean that trainees with no force sensitivity and less midichlorian count can't have high combat scores. 

## Limitations:
- The conclusion made above are subjected to certain limitations.
- Limited size of the dataset reduces the validity of the conclusions.
- Several missing values are in the dataset.
- It is a synthetic dataset.

## Future Scope:
- With a bigger and valid dataset clear conclusions can be made and a reliable variables of combat score can be found.
