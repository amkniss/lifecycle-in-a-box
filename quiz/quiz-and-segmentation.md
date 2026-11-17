# The Skin Quiz and the Segment Map

The quiz exists to do two jobs: give the customer a routine she trusts, and give the program the three facts that change what a flow should say. Three questions only. Every extra question costs completion, so a question has to earn its place by changing an email.

## Questions
1. **What is the one thing you want to change?** Dark spots / Fine lines / Sensitivity and redness / Breakouts
2. **How does your skin usually feel by midday?** Dry / Oily / Both, depends on the zone / Comfortable
3. **What does your current routine look like?** Just cleanser / Cleanser and moisturizer / A full routine with actives / Nothing consistent

## Answer to segment map

| Answer | Segment tag | What changes |
|---|---|---|
| Concern: Sensitivity | `concern_sensitivity` | Welcome email leads with tolerance protocol; browse abandon swaps guarantee creative for the buffered-formula explainer; post-purchase day-10 email arrives at day 7 instead |
| Concern: Dark spots | `concern_spots` | Welcome timeline sets week 8 to 12 expectation (spots move slower); winback subject line references the longer timeline |
| Skin: Dry | `skin_dry` | Post-purchase adds the moisturizer sandwich instruction; subscription nurture suggests cleanser add-on at cycle 2 |
| Current routine: Full actives | `routine_actives` | Welcome email 2 is replaced with the "what to pause" email, because her risk is interaction, not underuse |
| Current routine: Nothing consistent | `routine_starter` | Routine card is simplified to three steps total; day-10 check-in arrives at day 5 |

## Rules
- Quiz answers are properties on the profile, set once, and every flow reads them. A flow that ignores the quiz is a bug, not a variant.
- Quiz completers who do not buy enter the same welcome flow with the quiz version. There is no separate "quiz non-buyer" program to maintain.
- The quiz promise is kept in the data: if the quiz says "your routine in 30 seconds", the result page shows a routine, not a product grid with a discount banner. Message match is a retention feature.
