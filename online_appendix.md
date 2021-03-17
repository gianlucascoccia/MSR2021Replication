# UNDER CONSTRUCTION

# Topics description

## Stack Overflow topics

### App architecture

Questions in this topic discuss the fundamental logical structure of the desktop application in terms of, e.g., routes, views, and components. An example of this kind of questions is *'AngularJS $routerProvider not working properly in node-webkit'*, in which one developer asks for help in configuring the AngularJS router included in his application. Noticeably, the names of several JavaScript frameworks appear among the top words of this topic. Indeed, during JavaScript application development, it is common practice to adopt such frameworks to properly structure the application architecture when the logic becomes more extensive and difficult to maintain.

**Considerations:**
  * Desktop web application development requires the usage of abstractions and frameworks to properly manage the application's logical structure when dealing with growing application complexity.

**Examples:**
  * 1) https://stackoverflow.com/questions/20112297/angularjs-routerprovider-not-working-properly-in-node-webkit
  * 2) https://stackoverflow.com/questions/36017543/what-is-the-best-way-to-communicate-from-angular2-to-electron-and-back
  * 3) https://stackoverflow.com/questions/45700041/react-router-redirect-not-working-at-all-using-react-redux-electron


### Build & deploy

This topic comprises questions about the build process of desktop web apps, whose ultimate goal is to create build artifacts that can be distributed and executed on multiple platforms. An instance of this type of question is *'What are some mechanisms to package cross-platform Electron apps in a single build?'*. The presence of this topic among the most discussed ones is, at a first glance, contrasting with one of the main touted strengths of desktop web app frameworks: the possibility of developing an application in a single language while still being able to easily distribute it on multiple platforms. To investigate the matter more in-depth, we decided to conduct a manual analysis of questions relevant to this topic. From it, we noted that indeed developers require clarifications on these subjects even though desktop web app frameworks are designed to simplify deployment on multiple platforms due to the fact that developers often have specific requirements for the deployment of their applications on some platforms (e.g., *'How to deploy an Electron app as an executable or installable in Windows'*) or necessitate to include native libraries in their product and thus have to follow more elaborate build processes (e.g., *'Unable to load some native node js modules with electron 4.0.6 on Windows'*). 

**Considerations:**
  * Despite frameworks' efforts to simplify deployment across multiple platforms, developers often ask for help regarding the build and deploy processes.
	
 **Examples:**
  * 1) https://stackoverflow.com/questions/33152533/bundling-precompiled-binary-into-electron-app
  * 2) https://stackoverflow.com/questions/39225801/electron-packager-on-windows-does-nothing
  * 3) https://stackoverflow.com/questions/40593492/why-wont-electron-packager-bundle-node-modules-that-are-listed-in-package-js

### Client-server

this topic groups questions asking for clarification regarding interactions between the desktop web app and a remote server. For instance, in the post *'Electron: socket.io can receive but not emit'* a developer states that he is *'creating an Electron application that uses Socket.io to communicate to a server application'* and asks for help in troubleshooting issues that arise when forwarding messages from one of the clients to the server. The presence of this topic reveals that desktop web apps are often not developed in isolation but serve as an (additional) client-side interface for existing applications and services. This is in line with one of the main advantages offered by desktop web app frameworks, namely the possibility of reusing the already possessed web development skills to develop desktop applications. 

**Considerations:**
 * Desktop web applications are often developed as an additional front-end client for existing applications and services.

**Examples:**
  * 1) https://stackoverflow.com/questions/40623356/electron-app-that-opens-a-server-or-using-sockets-over-the-web
  * 2) https://stackoverflow.com/questions/45044189/node-js-multicast-client
  * 3) https://stackoverflow.com/questions/50081691/send-media-stream-to-clients-from-server
  
### Databases  
  
This topic contains questions relating to the persistent storage of data, by means of databases (e.g., *'nedb with electron and angularjs'*) or through the mechanisms offered by the browser (e.g., *'Auto-sync JS environment with LocalStorage or IndexedDB?'*). The presence of this topic highlights the importance of persistent data storage solutions in the development of desktop web apps.
  
**Considerations:**
  * 

**Examples:**
  * 1)   
  * 2) 
  * 3) 
  
### Dependencies
  
This topic collects questions dealing with issues related to the inclusion of libraries or other software dependencies. An example is the post *'Requiring node modules in ionic + electron (5.0.0) desktop application'*. The ability to reuse existing web development libraries for desktop applications is advertised as one of the major strengths of desktop web app frameworks. Hence, we deemed it appropriate to investigate the reasons behind the presence of this topic among the most discussed on Stack Overflow. Conducting a manual analysis of related questions, we identified two main reasons: firstly, as specified in the official Electron faq (https://www.electronjs.org/docs/faq), the way these frameworks integrate the node.js backend and the frontend browser instance can result in compatibility issues when employing some popular libraries (e.g., JQuery or AngularJS), which require additional setup steps to be correctly integrated; secondly, it is common practice in the JavaScript ecosystem to use dependency managers, i.e., software libraries that assist in the integration of multiple external libraries. Integrating these within desktop web apps is not always straightforward. In both cases, solving these issues requires manually tweaking configuration files of libraries, frameworks, or underlying components (e.g., configuration files of the node.js backend server). Required edits are mostly specific for each library, hence deep knowledge of the involved technologies is necessary. For instance, the answer to the question *'Error: Can't resolve 'electron-is-dev' in electron & typescript & webpack project*' reports the need to configure the webpack.config.js file in order to integrate Electron with the Webpack module bundler. 

**Considerations:**
  * 

**Examples:**
  * 1)   
  * 2) 
  * 3) 


## GitHub Topics

