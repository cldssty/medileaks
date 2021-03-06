Medileaks
---------

Medileaks aims to do the following: 

1. become the largest searchable repository with easy-to-read comparisons and summaries of medical best practice guidelines for every single aspect of medical care from surgery to all types of mental health diagnostics, prescription of medication and therapy. 

2. publish patient ratings and reports of malpractices/reviews for specific medical procedures, clinicians and departments that are not controlled by the clinicians or hospitals in any way.

3. predict success rates of medical procedures by training machine learning algorithms on large datasets.

There are a lot of problems that need to be solved before this can be done, such as how to get our hands on the right amount of data. Some of the main problems are outlined below. 

Best practices in medical care 
----------

Preliminary googling tells me that there isn't a universal standard of medical care across all types of medical care. Each hospital/practice has their own best practice guidelines that may differ. Even then, not all areas of medical care are covered. 

**1. Why do we want to make best practice guidelines open to the public?**

If patients know what to expect from a medical procedure or appointment, then they are more equipped to protect themselves against medical malpractices or sloppy practices. 

They can also refer to it when choosing between doctors. This happens a lot particularly in mental health. For instance, when choosing a suitable psychiatrist, it is often good to know how much they care about best practices when diagnosing and prescribing medication (with side effects) to patients. 

**2. Why aren't existing best practice guidelines enough?**

They do not necessarily cover all aspects of medical care. Even when multiple sets of guidelines cover the same area of medical practice, they do not necessarily agree. For instance, the [NICE](https://www.nice.org.uk/guidance/ng87) guidelines for ADHD treatment do not mention that the doctor needs to monitor a patient's heartrate while they are on methylphenedate, while it is a recommended step in the [Health guidelines by the Queensland government](https://www.health.qld.gov.au/__data/assets/pdf_file/0028/444367/adult-adhd-gl.pdf). 

This is not to say that the NICE guidelines are erroneous, but if a patient were aware of the existence of a set of perhaps stricter guidelines for what they are going through, they can decide whether they want to potentially choose another clinic, or consult their doctor on the possibility of adding that step if they are worried. 

Hoping to be able to compare best practice guidelines across any set of hospitals on this site.

**3. Why aren't there universal standards for some forms of medical practices?**

To be added.

**4. How do you go about finding guidelines and research papers?**

Probably use of web scraping tools, but need to think of more time-efficient methods.

**5. How would people query the database?**

Examples to be added. 

**6. There is so much information. How would you be able to get through all of that if you don't have much time, which is usually the case?**

I will be using some text summarisation algorithms and data visualisation tools so that the users are shown answers to their main concerns, which are defined by personal experience, feedback from users and research.

Another solution to deal with comprehending big data is to train machine learning algorithms on medical procedure data so that they can detect anomalies. For instance, Loubna Bouarfa from TU Delft has used Machine Learning algorithms to find patterns in surgical operations[1] in order to detect anomalies in surgery. A record of mistakes detected over time can then be helpful for making predictions for the success rate of surgical or any medical procedure.

Predictions
----------

It is often helpful to predict the success rate of any medical procedure. One can use a variety of data such as clinician performance records, effectiveness of medication etc. to come up with predictions using machine learning algorithms. 

One of the problems are, however, to get access to large enough datasets for every kind of medical procedure. For instance, the NHS provide open datasets for *some* procedures, such as surgical performance data, but even then the datasets can be quite small, so if machine learning algorithms are used to do predictions then they won't be accurate.  

One also has to figure out how performance measurements (or other measurements) are done. For instance, how are mental health service performances measured? One possibility is to compute the proportion of in-patients that become out-patients and then discharged over some fixed time period that is considered a 'good' 'recovery' time. 

As mentioned above, sometimes we can use machine learning algorithms to find mistakes in medical procedures. That could potentially be an accurate way of measuring performance of a clinician. 

**1. Why are datasets small?**

There are many reasons. Take the neurosurgical performance dataset as an example. A lot of the clinics aren't rated because the sites are 'not within the scope of the national neurosurgery audit'. So we need to find out a way to get around that as well. 

Anonymous reviews and ratings 
----------

**Existing tools**

Most existing review and rating systems for hospitals and medical care are too general and disorganised. We often do not know how users come up with ratings and therefore do not know how to interpret a rating. A 5 star could mean good A&E service or something else. 

Similarly, reviews are often not organised into departments, services and doctors. Even if it is, for instance in [doctify](https://www.doctify.co.uk), people can only submit reviews if they've been given a token by the doctor they are reviewing. That means that the doctor can control who writes reviews on their profile on the site, which is exactly what this site does NOT want. 

**What we do here**

1. Ratings

In Medileaks, we'd like ratings to be specific to particular medical procedures. There might still be an overall rating for a hospital for example, but it should be easy for people to see how we've combined specific ratings to get it. 


2. Reviews

Here, we'd like to focus on reports on medical malpractices supported with evidence if possible. While positive reviews are important, negative ones are effective in protecting prospective patients.

Similary, text summarisation algorithms can be used to summarise specific reviews to give users an overall impression of a hospital or a clinician, but it should again be easy for them to access the specific reviews that are taken into account by the summary. 

**However, it is difficult to verify the validity of such reports if there is no evidence. And even if evidence is available, it is not always easy to check whether it is valid evidence either.**

Algorithms and software used
----------

Please refer to the [wiki](https://github.com/cldssty/medileaks/wiki/Text-Summarisation) for more details. 

Legal Considerations
----------

This needs to be GDPR compliant and other things. Please refer to the [wiki](https://github.com/cldssty/medileaks/wiki/Legal-Considerations) for more details. 

References
----------
[1] Loubna Bouarfa. Recognizing surgical patterns. 30 May 2012:TU Delft Aula.

Contributing 
----------
Contributions are very welcome. Please first refer to the [Contributing Guidelines](https://github.com/cldssty/medileaks/wiki/Contributing).




