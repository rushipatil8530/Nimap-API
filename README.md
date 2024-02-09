# Nimap-API
# Django Python Machine Test

## Overview
This project is a machine test for Django Python, focusing on designing APIs using a REST framework within a Django project. The APIs manage three main entities: Users, Clients, and Projects.

## Task Summary
The completed tasks include:

- **Register a Client:** Implement a POST request to register a new client with input fields for the client's name. Upon successful registration, the system generates a unique client ID along with other details such as creation timestamp and creator information.
  
- **Fetch Clients Info:** Implement a GET request to fetch information about all clients registered in the system. The response includes details such as client ID, client name, creation timestamp, and creator information.
  
- **Edit/Delete Client Info:** Implement endpoints to update and delete client information. The PUT/PATCH request allows updating the client's name, and the DELETE request removes the client from the system. Proper status codes are returned upon successful deletion.
  
- **Add New Projects for a Client and Assign Users:** Implement a POST request to create a new project for a specific client. The request body includes the project name and a list of users to be assigned to the project. Users are assigned to projects by their unique IDs. The response includes details of the created project along with the assigned users and client information.
  
- **Retrieve Assigned Projects to Logged-in Users:** Implement a GET request to retrieve all projects assigned to the logged-in user. The response includes details such as project ID, project name, creation timestamp, and creator information.

## Additional Considerations
- The system architecture considers scalability, allowing for many users, clients, and projects.
- Relationships between entities are properly managed, ensuring that a client can have multiple projects, and a project can be assigned to multiple users.

## Repository
The code and documentation for this project can be found in the Git repository. Please refer to the repository for detailed implementation and setup instructions.

[Link to Git Repository](<https://github.com/rushipatil8530/Nimap-API>)

For any further inquiries or clarifications, please feel free to reach out.

Best regards,  
Rushikesh Patil

## Clients URLs

### List and Create Clients
- `GET /clients/`: List all clients
- `POST /clients/`: Create a new client

### Retrieve, Update, and Delete Clients
- `GET /clients/:id/`: Retrieve details of a specific client
- `PUT /clients/:id/`: Update details of a specific client
- `PATCH /clients/:id/`: Partially update details of a specific client
- `DELETE /clients/:id/`: Delete a specific client

## Projects URLs

### List and Create Projects
- `GET /projects/`: List all projects
- `POST /projects/`: Create a new project

### Retrieve, Update, and Delete Projects
- `GET /projects/:id/`: Retrieve details of a specific project
- `PUT /projects/:id/`: Update details of a specific project
- `PATCH /projects/:id/`: Partially update details of a specific project
- `DELETE /projects/:id/`: Delete a specific project
