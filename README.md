# GearGuard: The Ultimate Maintenance Tracker

This repository contains our team's solution for the Odoo Hackathon. We are a team of four developers dedicated to building a maintenance management system that connects Equipment, Teams, and Requests.

## Team Members
* Patel Darsh
* Panchal Om
* Rasania Mihir
* Rathod Dhaval

---

## Problem Statement
The objective is to develop a maintenance management system (GearGuard) that allows a company to track its assets (machines, vehicles, computers) and manage maintenance requests.

### Core Functional Areas

#### 1. Equipment Management
* **Central Database**: Serves as a central repository for all company assets.
* **Technical Details**: Tracks details including Name, Serial Number, Purchase Date, and Warranty information.
* **Asset Tracking**: Supports tracking by Department or by Employee.
* **Responsibility**: Each piece of equipment is assigned a dedicated Maintenance Team and a default technician.

#### 2. Specialized Maintenance Teams
* **Team Definition**: Ability to define specialized teams such as Mechanics, Electricians, or IT Support.
* **Workflow Logic**: Specific users (technicians) are linked to teams; only team members should pick up requests assigned to their team.

#### 3. Maintenance Requests
* **Request Lifecycle**: Handles the progression of repair jobs.
* **Request Types**: 
    * Corrective: Unplanned repairs for breakdowns.
    * Preventive: Planned routine checkups.
* **Key Fields**: Tracks subjects, affected equipment, scheduled dates, and repair duration.

### Functional Workflows

#### Flow 1: The Breakdown (Corrective)
1. **Request Creation**: Any user can create a maintenance request.
2. **Auto-Fill Logic**: Selecting an equipment automatically fetches the category and Maintenance Team from the equipment record.
3. **Execution**: The request starts in the New stage, moves to In Progress, and finishes at the Repaired stage.
4. **Recording**: Technicians record the Hours Spent (Duration) upon completion.

#### Flow 2: The Routine Checkup (Preventive)
1. **Scheduling**: A manager creates a request with the type Preventive and sets a Scheduled Date.
2. **Visibility**: These requests appear on the Calendar View for technician awareness.

---

## Technical and UI Requirements
* **Maintenance Kanban Board**: A workspace for technicians grouped by stages (New, In Progress, Repaired, Scrap) with drag-and-drop functionality.
* **Visual Indicators**: Kanban cards show technician avatars and display red indicators if a request is overdue.
* **Smart Buttons**: Equipment forms must include a Maintenance button showing the count of open requests and providing access to related history.
* **Scrap Logic**: Moving a request to the Scrap stage indicates the equipment is no longer usable.
* **Reporting**: Pivot or Graph reports showing the number of requests per team or equipment category.
