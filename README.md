Medileaks
---------

Medileaks is an ongoing project that aims to do the following: 
1. 
2. 
3. 

A universal standard of medical care 
----------

Preliminary googling tells me that there isn't a universal standard of medical care across all types of medical care. Each hospital/practice has their own best practice guidelines that may differ. Even then, not all areas of medical care are covered. 

**1. Why do we want a universal standard?**

If patients know what to expect from a medical procedure or appointment, then they are more equipped to protect themselves against medical malpractices or sloppy practices. 

They can also refer to it when choosing between doctors. This happens a lot particularly in mental health. For instance, when choosing a suitable psychiatrist, it is often good to know how much they care about best practices when diagnosing and prescribing medication (with side effects) to patients. 

**2. Why aren't existing best practice guidelines enough?**

They do not necessarily cover all aspects of medical care. Even if they do, their guidelines may differ from guidelines from other practices. For instance, the NICE guidelines for ADHD treatment do not mention that the doctor needs to monitor a patient's heartrate while they are on methylphenedate, while it is a recommended step in the [insert clinic] guidelines. 

This is not to say that the NICE guidelines are erroneous, but if a patient were aware of the existence of a set of perhaps stricter guidelines for what they are going through, they can decide whether they want to potentially choose another clinic, or consult their doctor on the possibility of adding that step if they are worried. 

**3. Why aren't there universal standards for some forms of medical practices?**

There are many reasons but one reason is that it's too complicated. For instance, it is too difficult to come up with a general one for all different types of surgery because there are too many and they are too different. 

**4. Are there ways to solve that?**

There has been research done on this particular example for instance, and I'm sure there is research done for other examples as well but I haven't looked at them. 

[insert name] from TU Delft has used Machine Learning algorithms to find patterns in surgical operations to come up with a standardised workflow for them. She's trained an HMM on 10 LapChop operations and used a variety of algorithms to do the pattern recognition. 

So if we can round up existing standards and solutions to the lack of universal standards such as the research results mentioned above, centralise them and make the repository easily searchable, then patients can know not only what is available at the moment, but what can potentially be standardised in the future. 

**5. How do you go about finding guidelines and research papers?**

Probably use of web scraping tools, but need to think of more time-efficient methods.

**6. How would people query the database?**

Examples to be added. 

**7. There is so much information. How would you be able to get through all of that if you don't have much time, which is usually the case?**

I will be using some text summarisation algorithms and data visualisation tools so that the users are shown answers to their main concerns, which are defined by personal experience, feedback from users and research.

Predictions
----------

It is often helpful to predict the success rate of any medical procedure. One can use a variety of data such as clinician performance records, effectiveness of medication etc. to come up with predictions using machine learning algorithms. 

One of the problems are, however, to get access to large enough datasets for every kind of medical procedure. For instance, the NHS provide open datasets for *some* procedures, such as surgical performance data, but even then the datasets can be quite small, so if machine learning algorithms are used to do predictions then they won't be accurate.  

One also has to figure out how performance measurements (or other measurements) are done. For instance, how are mental health service performances measured? One possibility is to compute the proportion of in-patients that become out-patients and then discharged over some fixed time period that is considered a 'good' 'recovery' time. 

**1. Why are datasets small?**

There are many reasons. Take the neurosurgical performance dataset as an example. A lot of the clinics aren't rated because the sites are 'not within the scope of the national neurosurgery audit'. So we need to find out a way to get around that as well. 

Anonymous reviews and ratings 
----------

**Existing tools**

Most existing review and rating systems for hospitals and medical care are too general and disorganised. We often do not know how users come up with ratings and therefore do not know how to interpret a rating. A 5 star could mean good A&E service or something else. Similarly, if a hospital does not receive all the stars, we do not know why that is. It is important to know why somebody is not satisfied with medical care because it can help prospective patients avoid the problems that have led to the deficit of stars. 

Similarly, reviews are often not organised into departments, services and doctors. Even if it is, for instance in doctify, people can only submit reviews if they've been given a token by the doctor they are reviewing. That means that the doctor can control who writes reviews on their profile on the site, which is exactly what this site does NOT want. 

**What we do here**

In Medileaks, we'd like ratings and reviews to be specific to particular medical procedures. There might still be an overall rating for a hospital for example, but it should be easy for people to see how we've combined specific ratings to get it. Similary, text summarisation algorithms can be used to summarise specific reviews to give users an overall impression of a hospital or a clinician, but it should again be easy for them to access the specific reviews that are taken into account by the summary. 

Algorithms and software used
----------

*Text Summarisation Algorithms*

to be added.

*Data Visualisation Tools*

to be added.

Contributing 
----------
here you need to set small problems in the issue tracker and label them easy or good first time contribution 
problems have to be well-defined, extremely clear and can be done with low effort so that people get satisfaction quickly
you should also respond to contributions quickly
and break your project up into many small pieces so that people can choose what to work on
you need to find a way to make your issue tracker populous though
I think you should also manage your issue tracker so that there aren't two conflicting solutions to the same problem and you don't encourage two solutions if they are going to clash 
or if you do, warn contributors beforehand




