# Week 3 Report: RegistrarQueue


## 1. Title details

| | |
| --- | --- |
| **App** | RegistrarQueue |
| **Setting** | MSU-IIT Registrar's Office (document requests and claiming) |
| **Name** | Sammy R. Ditanongun |
| **Student ID** | 2024-0709 |
| **Section** | CS3B |
| **Date** | 10/26/2026 |
| **Pull request** | https://github.com/slyoh26/CCC181/pull/3 |

## 2. Personas

Full personas are in [personas.md](personas.md).

**Dani, the person waiting.** A 21-year-old 3rd-year Microbiology student who requests and claims documents at the registrar.
- Quote *(interview)*: "Papansin pud ka dapat, pero other than that, ang pagclaim lang sa reqs, sometimes magwait paka kadali." (You also have to make yourself noticed, but when claiming your requests you sometimes wait a little.)
- Top tasks: join the queue (FR-01), check my number and people ahead (FR-02), see when I am called (FR-03), leave the queue (FR-04). ⚠ Use your real IDs.

**Mrs. Reyes, the staff member.** A 30-year-old registrar staff member who receives requests and receipts and hands out documents at a busy counter on a shared office PC.
- Quote *(interview)*: "It takes time especially pag daghan na ang ga pila." (It takes time, especially when many people are lining up.)
- Top tasks: see the waiting list in order (FR-05), call the next person (FR-06), mark served (FR-07), mark no-show (FR-08), filter by document (FR-09).

## 3. Screens

The screenshots show the running app, at phone width (375 px) and laptop width.

**Join**

![Join on a phone](screenshots/join-phone.png)
![Join on a laptop](screenshots/join-laptop.png)

Used by Dani to get her number. Covers FR-01. 

**My place**

![My place on a phone](screenshots/myplace-phone.png)
![My place on a laptop](screenshots/myplace-laptop.png)

Used by Dani to see her number, status and how many people are ahead, and updates itself every 10 seconds. Covers FR-02, FR-03, FR-04. 

**Staff dashboard**

![Staff dashboard on a phone](screenshots/staff-phone.png)
![Staff dashboard on a laptop](screenshots/staff-laptop.png)

Used by Mrs. Reyes to call, serve and mark no-show, and to filter by document. Covers FR-05 to FR-09. 

## 4. Design decisions

1. **The ticket number and position are the largest things on My place.** In her interview, Dani said you have to be "papansin" to be noticed, because the order of the line is not visible. Showing her number and "3 people ahead of you" in large text means she can see her place from her phone without speaking up (Dani's rule 1, and the My place wireframe).
2. **"Call next" is the biggest element on the staff dashboard, and Serve only appears on called tickets.** Mrs. Reyes uses Call next most often during the morning rush, so it is a full-width button. My usability test found that Serve was available on tickets that had not been called, so I hid it for those rows and made the server reject it too, which prevents serving the wrong person (Mrs. Reyes's rules 1 and 4).
3. **The Join form is short and uses the words students use.** The self-review found that the wireframe said "ticket" and used long document names, while people at the registrar say "number" and "TOR" and "COR". The form has the button "Get my number" and lists "Transcript of records (TOR)" and "Certificate of registration (COR)". I added one setting-specific field, "I am a" (Student or Alumni), because students and alumni both line up for documents (Dani's rule 3).

## 5. Self-review

Full review in [feedback.md](feedback.md). The main problems and changes:

- **Join:** the wording did not match the setting (match with the real world). I changed "ticket" to "number" and added TOR and COR to the document names.
- **My place:** the page did not show that it updates itself or what to do when called (visibility of system status). I added "This page updates automatically" and a message for the Called state that says to go to the counter with the receipt.
- **Staff:** on the phone, Serve and No-show were off-screen behind the sideways scroll (recognition rather than recall). I moved the Actions column next to the number and sorted Called tickets first. ⚠ Say whether you updated the wireframes or kept the originals.

## 6. Accessibility

Full results in [accessibility.md](accessibility.md).

| Screen | Lighthouse Accessibility score (mobile) |
| --- | --- |
| Join | 100 |
| My place | 100 |
| Staff | 95 |

![Join Lighthouse score](screenshots/lighthouse-join.png)
![My place Lighthouse score](screenshots/lighthouse-myplace.png)
![Staff Lighthouse score](screenshots/lighthouse-staff.png)

The most important issue I fixed:  the Serve and No-show buttons were about 31 px tall with `btn-sm`, so I replaced them with a 44 px minimum height and wider spacing for touch. On the Staff page, Lighthouse reports one remaining contrast issue (background and foreground colors do not have a sufficient contrast ratio). 

## 7. Usability test


| Task | Result |
| --- | --- |
| 1. Join the queue | Finished without help in about 50 seconds. Paused at the "I am a" field and asked whether to pay before getting a number. |
| 2. Find number and people ahead | Finished in about 5 seconds because the number is so large. |
| 3. Call next and serve as staff | Finished in about 1 minute. Hesitated because every row had a Serve button, including tickets that had not been called. |

**Improvement:** Serve now only appears on tickets with the status Called, and the server rejects a Serve request for any other ticket.

| Before | After |
| --- | --- |
| ![Before](screenshots/before.png) | ![After](screenshots/after.png) |

## 8. Reflection


The hardest part was getting the Git and GitHub setup right (cloning into the right folder, the branch, and signing in to push), and then keeping the routes and template names consistent so that `url_for` did not fail. I also found it hard to turn the interview notes into design rules, because I had to decide which things people actually said mattered.

When the data moves to PostgreSQL in Week 4, I will need to change how tickets are found and numbered, because right now they live in a Python list that resets every time the server restarts, and the number is the last ticket plus one. The helper functions `find_ticket` and `people_ahead` are in one place, so I can change them without touching the templates. I also want to explain the payment and receipt step on the Join page, since the usability test showed that people did not know when to pay.

## 9. Declaration

- **Figma Make** was used to generate the first draft of the wireframes, which I then edited and exported.
- **Claude (Anthropic AI assistant)** was used for step-by-step guidance, reference code for the Flask routes and templates, and drafts of the personas, the self-review, the usability test notes and this report. I reviewed and corrected the drafts, ran and tested the code myself, and took all screenshots.
- Chrome Lighthouse was used for the accessibility scores.
