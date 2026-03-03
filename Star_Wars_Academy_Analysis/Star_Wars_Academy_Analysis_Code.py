import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("star_wars_academy.csv")
pd.set_option('display.max_columns',None)

#Relation between force sensitivity and combat score
#For force sensitive trainees
print("Force Sensitive:")
forceusers=df[df['Force_Sensitive']==True]
combatscore1=forceusers['Combat_Score']
forceavg=combatscore1.mean()
forcemedian=combatscore1.median()
forcenames=list(forceusers['Name'])
forcecombat=list(combatscore1)
plt.barh(forcenames,forcecombat,color='red',label='Force Sensitive')
print('The average combat score for force sensitive trainees is', forceavg)
print('The median combat score for force sensitive trainees is', forcemedian)


#For non force sensitive trainees
print("\nNon Force Sensitive:")
nonforceusers=df[df['Force_Sensitive']==False]
combatscore2=nonforceusers['Combat_Score']
nonforceavg=combatscore2.mean()
nonforcemedian=combatscore2.median()
nonforcenames=list(nonforceusers['Name'])
nonforcecombat=list(combatscore2)
plt.barh(nonforcenames,nonforcecombat,color='blue',label='Non force sensitive')
print('The average combat score for non force sensitive trainees is', nonforceavg)
print('The median combat score for non force sensitive trainees is', nonforcemedian)

plt.title('Comparison of combat score over force sensitivity')
plt.xlabel('Combat Scores')
plt.ylabel('Trainees Names')
plt.legend()
plt.savefig('Combat score vs Force Sensitivity.png')
plt.show()


#Relation between Midichlorian Count and Combat Score
df1=df[['Midichlorian_Count','Combat_Score']]
df1=df1.sort_values(by='Midichlorian_Count',ascending=False)
cor=df1['Midichlorian_Count'].corr(df1['Combat_Score'])
print('The correlation coefficient between midichlorian count and combat score is ',cor) 
print('\nIt can be also manually verified with:')
print(df1)
plt.scatter(df1['Midichlorian_Count'],df1['Combat_Score'])
plt.title('Relationship of Midichlorian Count and Combat Score')
plt.xlabel('Midichlorian Count')
plt.ylabel('Combat Score')
plt.savefig('Relationship of Midichlorian Count and Combat Score.png')
plt.grid(True, alpha=0.3)
plt.show()

#Relation between age and combat score
df2=df[['Age','Combat_Score']]
df2=df2.sort_values(by='Age',ascending=False)
crr=df2['Age'].corr(df2['Combat_Score'])
print('The correlation coefficient between age and combat score is ',crr) 
print('\nIt can be also manually verified with:')
print(df2)
plt.scatter(df2['Age'],df2['Combat_Score'])
plt.title('Relationship of Age and Combat Score')
plt.xlabel('Age')
plt.ylabel('Combat Score')
plt.savefig('Relationship of Age and Combat Score.png')
plt.grid(True, alpha=0.3)
plt.show()

#Relation between planet and combat score
a=df.groupby(df['Planet'])['Combat_Score'].mean().sort_values(ascending=False)
print('Each planet and it''s average combat score is listed below:')
print(a)
a.plot(kind='bar')
plt.title('Relation between planet and combat score')
plt.xlabel('Planet')
plt.ylabel('Combat_Score')
plt.xticks(rotation=45)
plt.savefig('Relation between planet and combat score.png')
plt.show()

#Relation between lightsaber colour and combat score
a=df.groupby(['Lightsaber_Color'])['Combat_Score'].median().sort_values(ascending=False)
print('The median distribution of combat score with lightsaber color is shown below:')
print(a)
a.plot(kind='bar')
plt.title('Median distribution of combat score with lightsaber color')
plt.xlabel('Lightsaber Color')
plt.ylabel('Combat Score')
plt.savefig('Median distribution of combat score with lightsaber color.png')
plt.show()
