**Pred_quali_runs**

is the first first version of trying to predict quali times.
It is good at predicting 0 runs and decent at predicting first quali runs but does lack in rest of the predictions.
This also trained on the whole dataset. Included 1950 results. <br> <br>
And with that you can predict some fun stuff like what time Senna would have gotten whit mercedes in Abu Dhabi.  
Even tought the predictions are around 10 seconds of the actual time I think you can get the idea what kind of results he could put up in today's car

**Modern_era_quali_pred**

 is the second version of the Pred_quali_runs. Main goal was to enhance the 0 prediction and 
first quali run prediction to be more precise with the first runs but also with the rest of the runs.
Spoiler, that did not end up happening and is actually worse than the first version. 
Even with the first version having some mistakes that I did not fix.

Anyway, spend most of the time trying to find a way to fix custom loss to be better. And... Well it did not happen :]

**pred_race_winner**

This was final attempt to make something work well by using simple sklearn library models. 
Goal was to predict position for each driver and fastest lap time for each driver.
Again. had issues predicting time and this point I realized that predicting time is actually really damn difficult to do.

But I got r score of 0.34 ish for the position prediction. Could get it better that is for sure but, I will leave it to that.

**Some thoughts**


To be honest, I'm little-bit disappointed that I could not get good model to predict qualifying times.
<br> But I had fun with this "small" project trying to learn what machine learning and deep learning is, 
and I'm hopefully that this is the career where I want to develop in the future. 

On to next database... What ever that might be...