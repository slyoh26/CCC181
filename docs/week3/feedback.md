# Week 3 self-review: RegistrarQueue wireframes

Reviewed against Dani's rules (large ticket number, auto-updating status in words, short Join form, say what she is there for) and Mr. Reyes's rules (Call next biggest, document type on every row, No-show one click away, buttons that name their ticket).

---

## Screen 1: Join (phone and laptop)

**Works well:** The form has only three labeled fields (name, email, document) and one full-width "Get a ticket" button, on both phone and laptop. Dani can tell what to do in under 5 seconds, and the form is clearly shorter than the Google Form she finds slow (her rule 3).

**Problem:** The words do not match how people at the registrar talk (*match between the system and the real world*). The registrar gives you a "number", and students refer to documents by their short names, TOR and COR. The wireframe says "ticket" on the button and shows only the long document names, so Dani has to translate.

**Change:** I will change the button to "Get my number" and list the options as "Transcript of records (TOR)", "Certificate of registration (COR)" and "Report of grades", so both the short and full names are visible. I will keep the short three-field form.

**Rules check:** Follows Dani's rule 3 (short form). Does not yet cover her rule 4 (saying whether she is claiming or requesting), which depends on which queue I decide to build.

---

## Screen 2: My place (phone and laptop)

**Works well:** The ticket number (#14) is by far the largest element, and "3 people ahead of you" is the second largest, on both phone and laptop. On the phone they are still at the top, so Dani sees them first even with one hand busy (her rule 1). "Leave the queue" is small and separated by a divider with a warning line, which prevents accidental taps.

**Problem:** The page does not show that it updates by itself, and it does not say what Dani must do when her status becomes "Called" (*visibility of system status*). She would not know whether to refresh the page, or where to go and what to bring once she is called.

**Change:** I will add a line under the status, "This page updates automatically", and a "Called" state that says "Go to the registrar counter now and bring your receipt". I will add a Called version of this screen to the wireframes.

**Rules check:** Follows Dani's rule 1 (big number) and shows the status in words, not only color. Only partly follows her rule 2, because the auto-update is not visible.

---

## Screen 3: Staff dashboard (phone and laptop)

**Works well:** "Call next" is a full-width black bar at the top, the largest element on both frames, so the action Mr. Reyes does most often is the easiest to reach (his rule 1). Each row shows the document type next to the number (his rule 2).

**Problem:** On the phone, the Actions column (Serve and No-show) is off-screen to the right, behind the sideways scroll. Staff would have to remember to scroll to find the buttons they use most after "Call next" (*recognition rather than recall*). Also, every row has identical "Serve" and "No-show" buttons that do not show which ticket they belong to, so on a busy counter the wrong ticket could be clicked.

**Change:** I will move the Actions column to the second position, right after the number, so the buttons are visible at 375 px without scrolling. On every button I will keep the ticket number in its accessible label (for example "Mark ticket 14 as served"), and I will sort the table with Called tickets first, then Waiting tickets by ticket number.

**Rules check:** Follows Mr. Reyes's rules 1 and 2. Partly breaks rule 3 on the phone, because No-show is not reachable without scrolling. Rule 4 (buttons that name their ticket) is not visible in the wireframe and will be done in the code.
