# Project Title
Tackling NYC Subway Delays: A Focus on Signal Failures

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Every New Yorker knows the pain of a delayed train. It's way more than just an inconvenience it can mess up your whole day, costing you time and money and energy. A huge piece of this problem comes from the subway's old-school signal system. Much of it is ancient, and when it breaks down, it slows down trains tremendously.

In this project, we're going to dig into the data to figure out exactly where these signal failures are the worst. The goal is to turn that data into a limpid image that can help lead to smarter, more targeted fixes.

## Stakeholder & User
*   **Primary Stakeholder:** The decision-makers at the MTA's Capital Planning department. These are the folks who decide where to spend the big bucks on system upgrades.
*   **End User:** The day to day Subway Operations and Maintenance teams. They're on the front lines and can use this information to better understand and tackle recurring problems.

## Useful Answer & Decision
*   **What we're doing:** This is a descriptive project. We're not predicting the future, we're painting a clear picture of what's happening right now.
*   **What we're delivering:** The main output will be an interactive dashboard that shows the biggest problem spots for signal failures.
*   **The decision it supports:** This dashboard will help the MTA make a tough but very important decision: "With a limited budget, which signal upgrades will help the most riders, right now?"

## Assumptions & Constraints
*   **Assumption:** We're trusting that the MTA's data on *why* a train was delayed is mostly accurate.
*   **Constraint:** We're working with publicly available data, so we won't have access to the MTA's internal, real-time systems.
*   **Constraint:** The data probably won't be perfect. We expect we'll have to do some work to clean it up and account for miscategorized delays.

## Known Unknowns / Risks
*   **Risk:** The public data might not be detailed enough. For example, it might just say "signal failure" without telling us the specific type of failure.
*   **Uncertainty:** How do you even measure the "impact" of a delay? A 5-minute delay during rush hour is a nightmare for thousands, while a 20-minute delay overnight affects far fewer people. We'll need to come up with a good metric for this, and we'll start by exploring both total delay minutes and "total passenger-minutes lost."

## Lifecycle Mapping
*   **Goal A:** Help prioritize signal upgrade projects → **Problem Framing (Stage 01)** → **Deliverable:** This project plan and a memo for our stakeholders.
*   **Goal B:** Find the signal failure hotspots → **Data Work (Stage 02)** → **Deliverable:** A clean dataset of subway delays.

## Repo Plan
*   **/data/:** This is where we'll keep the raw data files from the MTA.
*   **/notebooks/:** For our scratch work—exploring the data and trying out ideas.
*   **/src/:** For any polished, reusable code we write.
*   **/docs/:** For our stakeholder memo and final presentation, also stakeholder memo is in the repo.
*   **Cadence:** We'll be updating the project at least once a week.
