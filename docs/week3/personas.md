## Dani, the person waiting

> "Papansin pud ka dapat, pero other than that, ang pagclaim lang sa reqs, sometimes magwait paka kadali." *(interview)*
>
> *(English: "You also have to make yourself noticed, but other than that, when claiming your requests you sometimes wait a little.")*

| | |
| --- | --- |
| **Photo or sketch** |  [Dani, the person waiting](images/dani.jpg) |
| **Age, role and background** | 21, 3rd-year Microbiology student at MSU-IIT *(interview)*. Requests documents such as forms and records from the registrar and returns later to claim them.  Has classes during the day and fits the visit between them. Other people in the same line are alumni and other students *(observation)*. |
| **Goals** | 1. Claim the requested documents without wasting time at the counter. 2. Be served in a fair order without having to push to be noticed. 3. ⚠ Request the right document in as few steps as possible. |
| **Frustrations** | 1. Has to be "papansin" (make themselves noticed) to get attention *(interview)*, because there is no clear sign of who is next. 2. Waits when claiming, even though the document is already prepared by the time they return, because one staff member hands out the documents *(interview)*. 3. Waits around 5 minutes at the counter, especially when many people are claiming at once *(interview)*. 4. The line is often long, and the process takes several steps (fill in a paper form, pay the fees, return with the receipt, get a number, come back later) *(observation)*. 5. The online Google Form for requests can also be slow *(observation)*. |
| **Devices and context** |  Mostly a phone, on campus, standing at the registrar or walking between classes and the cashier. One hand is often busy holding the form and receipt. Mobile data may be slow. |
| **Tech comfort** |  Medium. Uses Google Forms and a phone daily, but loses patience with slow or long forms. |
| **Accessibility needs** | Small phone screen in bright sunlight, so text and buttons need to be large and high contrast. One hand busy. Possibly slow mobile data. |

### Scenario

 Dani returns to the registrar at 2:00 pm to claim the documents she requested yesterday. Several people are already crowded at the counter, and one staff member is handing out documents. In the past she had to push to be noticed, so this time she opens RegistrarQueue on her phone, chooses her document type, enters her name and email, and gets ticket #14. My place shows her number in large text and says there are 3 people ahead of her. She steps back from the crowd, and a few minutes later the status changes to "Called". She walks up to the counter and collects her documents.

### Top tasks in the app

 Replace the IDs with your own.

| Task | Screen | Requirement ID |
| --- | --- | --- |
| Join the queue for a document request or claim | Join | FR-01 |
| Check my ticket number and how many people are ahead | My place | FR-02 |
| See when my ticket has been called | My place | FR-03 |
| Leave the queue if I can no longer wait | My place | FR-04 |

### What this means for my interface

1. Because Dani said you have to be "papansin" to be noticed, My place must show her ticket number and how many people are ahead in large text, so the order is visible without speaking up.
2. Because the wait at the counter is short but unpredictable and depends on how many people are claiming, My place must update by itself and show the status in words ("Waiting", "Called"), so she can step away from the crowd.
3. Because one staff member hands out documents and the existing process is already long, the Join form must be short (name, email, document type) so it does not add to the wait.
4. Because her documents are already prepared when she returns, the Join screen should let her choose what she is there for, such as claiming documents versus requesting a new one.

---

## Mrs. Reyes, the staff member

> "It takes time especially pag daghan na ang ga pila."

| | |
| --- | --- |
| **Photo or sketch** | [Mrs. Reyes, Registrar staff](images/reyes.jpg) |
| **Age, role and background** |  30, registrar staff member who receives requests and receipts and hands out documents at the counter. Serves students and alumni all day, with the busiest rush in the morning. |
| **Goals** | 1. Serve people in the right order without arguments about who was first. 2. Quickly see who is next and which document they need. 3.  Keep the crowd at the counter under control during the rush. |
| **Frustrations** | 1. A long line of students and alumni at the counter at once *(observation)*. 2. Handling the paper form, the receipt, the number and the claiming of documents manually for every request . 3. People who leave without telling staff, so staff call numbers nobody answers. |
| **Devices and context** |  Shared office desktop or laptop at the registrar counter, with a mouse and keyboard. Talking to a student while using the screen, so actions must be quick and hard to click by mistake. |
| **Tech comfort** |  Medium. Comfortable with office software, but has no time to learn a complex tool during the rush. |
| **Accessibility needs** |  Shared PC, noisy and busy counter, frequent interruptions. Buttons must be large and clearly labeled. Status must not depend on color alone. |

### Scenario

 At 9:00 am the line at the registrar is long again. Mr. Reyes opens the staff dashboard on the counter PC and sees the waiting list in order, each ticket showing the document type. He clicks "Call next", and the next student's ticket changes to Called. When the student arrives, he hands over the documents and clicks "Serve". When a called number does not show up after a few minutes, he clicks "No-show" and moves to the next person.

### Top tasks in the app

 Replace the IDs with your own.

| Task | Screen | Requirement ID |
| --- | --- | --- |
| See the waiting list in order | Staff | FR-05 |
| Call the next person | Staff | FR-06 |
| Mark a ticket as served | Staff | FR-07 |
| Mark a ticket as no-show | Staff | FR-08 |
| Filter the list by document type | Staff | FR-09 |

### What this means for my interface

1. Because the rush is busy and staff talk to students while using the screen, "Call next" must be the biggest and easiest button on the dashboard.
2. Because staff must know what each person needs, every row must show the document type next to the ticket number.
3. Because people sometimes do not show up when called, "No-show" must be one click away, and the status must say it in words so it can't be confused with "Served".
4. Because the dashboard runs on a shared office PC, every action button must name its ticket number, so the wrong person is never served by accident.
