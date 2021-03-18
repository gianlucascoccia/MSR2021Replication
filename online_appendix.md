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
  * Desktop web apps often include database solutions to achieve persistent data storage. 

**Examples:**
  * 1) https://stackoverflow.com/questions/44966809/accessing-nedb-find-results
  * 2) https://stackoverflow.com/questions/47751983/electron-knex-sqlite-handling
  * 3) https://stackoverflow.com/questions/39752269/nw-js-node-webkit-where-is-sqlite-db-stored
  
### Dependencies
  
This topic collects questions dealing with issues related to the inclusion of libraries or other software dependencies. An example is the post *'Requiring node modules in ionic + electron (5.0.0) desktop application'*. The ability to reuse existing web development libraries for desktop applications is advertised as one of the major strengths of desktop web app frameworks. Hence, we deemed it appropriate to investigate the reasons behind the presence of this topic among the most discussed on Stack Overflow. Conducting a manual analysis of related questions, we identified two main reasons: firstly, as specified in the official Electron faq (https://www.electronjs.org/docs/faq), the way these frameworks integrate the node.js backend and the frontend browser instance can result in compatibility issues when employing some popular libraries (e.g., JQuery or AngularJS), which require additional setup steps to be correctly integrated; secondly, it is common practice in the JavaScript ecosystem to use dependency managers, i.e., software libraries that assist in the integration of multiple external libraries. Integrating these within desktop web apps is not always straightforward. In both cases, solving these issues requires manually tweaking configuration files of libraries, frameworks, or underlying components (e.g., configuration files of the node.js backend server). Required edits are mostly specific for each library, hence deep knowledge of the involved technologies is necessary. For instance, the answer to the question *'Error: Can't resolve 'electron-is-dev' in electron & typescript & webpack project*' reports the need to configure the webpack.config.js file in order to integrate Electron with the Webpack module bundler. 

**Considerations:**
  * Reuse of traditional web development libraries within desktop web apps is common, but their integration is not always straightforward

**Examples:**
  * 1) https://stackoverflow.com/questions/39295951/why-cant-i-use-functions-from-javascript-files-that-are-imported-by-require
  * 2) https://stackoverflow.com/questions/42737885/ionic-2-build-error-cannot-find-module-dist-build
  * 3) https://stackoverflow.com/questions/29806669/node-js-typescript-can-not-find-local-module

### Errors

This topic concerns those discussions in which assistance is requested regarding error messages encountered during application development or usage. An example of this kind of post is *'Electron: TypeError: Cannot create property default on symbol Symbol(nodejs.util.inspect.custom)'*.

**Considerations:**
  * Developers request assistance regarding a wide variety of they encounter during application development.  
  
**Examples:**
  * 1) https://stackoverflow.com/questions/55552637/cannot-read-property-getcontext-of-undefined-electron
  * 2) https://stackoverflow.com/questions/52311819/error-fs-readfilesync-is-not-a-function-using-electron
  * 3) https://stackoverflow.com/questions/35210957/node-webkit-unexpected-undefined-is-not-a-function-on-string-prototype-includ

### File manipulation

This topic groups those questions in which developers report issues related to the creation, access, and modification of local files and folders (e.g., *'Write file to disk from blob in electron application'*). It's reasonable to think that file manipulation is more important for desktop app development than traditional web programming

**Considerations:**
  * File manipulation is frequently used in desktop applications, less so in traditional web application development.
  * Developers often require assistance to perform file manipulation with the backend node.js APIs.
  
**Examples:**
  * 1) https://stackoverflow.com/questions/39395195/how-to-write-wav-file-from-blob-in-javascript-node
  * 2) https://stackoverflow.com/questions/36860397/loading-a-yaml-file-in-electron-app
  * 3) https://stackoverflow.com/questions/44718683/nodejs-print-file-with-child-process

### Inter-process communication

This topic concerns the communication between concurrent processes. Indeed, desktop web app frameworks use a two-layer architecture composed of a back-end server and a front-end app window. These are executed in two concurrent processes and the communication between the two must be handled by the developer. An example of this kind of question is *'Communicate between parent and child renderer process Electron JS''}. Reasonably, we can expect that most web developers are not familiar with the inter-process communication concepts and, therefore, turn to Stack Overflow for clarification'*.

**Considerations:**
  * Desktop web apps developers are often unfamiliar familiar with IPC concepts.
  
**Examples:**
  * 1) https://stackoverflow.com/questions/51347738/electron-ipc-reference-error
  * 2) https://stackoverflow.com/questions/48961023/handling-nodejss-child-process-in-electron-app
  * 3) https://stackoverflow.com/questions/47563511/angular-electron-ipc-communication-and-service-method-call

### Developer tools

These are questions asking for explanations on how to use existing development tools, such as code editors and debuggers, in the context of desktop web apps. An example is the Stack Overflow post *'How to debug Quasar Electron App with VS Code'*. Similarly to what has been observed for the Dependencies topic, by manually analyzing questions related to the topic, we found that some of the tools commonly used by developers (e.g., IDEs, debuggers) require additional configuration steps or workarounds to be used for desktop web app development. One example is in the answer to the question *'Debug typescript electron program in vscode'* in which, to enable the usage of the IDE built-in debugger within the Electron application, the necessary edits to multiple IDE and build process configuration files are described. 

**Considerations:**
  * Some commonly adopted developer tools (e.g., debuggers, IDEs) cannot be used out-of-the-box for desktop web application development.

**Examples:**
  * 1) https://stackoverflow.com/questions/38067606/debug-typescript-electron-program-in-vscode
  * 2) https://stackoverflow.com/questions/35810902/empty-electron-window-when-debugging-typescript-app-in-visual-studio-code?rq=1
  * 3) https://stackoverflow.com/questions/60214490/get-vscode-to-recognize-variable-is-being-used-in-different-javascript-file
    
### Page contents

This topic groups questions in which and manipulation of page contents are debated. An example is the post *'Prevent DIV from scrolling on DOM content change'*.

**Considerations:**
  * Libraries and frameworks are often employed to perform page contents manipulation.
  * Manipulation of page contents is also a common activiity in traditional web application development.

**Examples:**
  * 1) https://stackoverflow.com/questions/42138548/change-dom-with-electron-ipcrenderer
  * 2) https://stackoverflow.com/questions/40878197/change-form-action-url-using-javascript-from-a-html-value
  * 3) https://stackoverflow.com/questions/37675229/how-to-access-the-contents-of-an-iframe-in-nw-js

### Platform integration

This topic aggregates those questions in which the developer asks how to invoke native APIs (e.g., *'node-server-screenshot not working on live ubuntu server'*) or how to interact with hardware peripherals (e.g., *'Accessing USB devices from node-webkit?'*). This topic is of primary importance, given that integration with the underlying platform is one of the main advantages offered by desktop web app frameworks. Manual exploration of related questions reveals that developers often face difficulties when their application needs to support multiple platforms, as not all APIs and behaviors are standardized across platforms. One example is given in the *'ELECTRON: image file(.png) silent printing on Ubuntu'* Stack Overflow post, where the accepted answer points out the need to employ two different APIs to implement printing of documents on Windows and Ubuntu. Moreover, developers often experience difficulty in integrating the required software libraries to bridge between the web application and the underlying platform. This stems from the fact that existing Node.js native modules cannot be used as-is but needs to be recompiled before usage, as desktop web app frameworks employ a different application binary interface (https://www.electronjs.org/docs/tutorial/using-native-node-modules and https://www.npmjs.com/package/nw-gyp).

**Considerations:**
  * Developers face difficulties when supporting multiple platforms due to: (i) inconsistent APIs across platforms and (ii) difficulties in integrating native modules into the desktop web application.
  
**Examples:**
  * 1) https://stackoverflow.com/questions/39812836/access-xinput-events-particularly-pen-pressure-in-electron
  * 2) https://stackoverflow.com/questions/22385116/accessing-usb-devices-from-node-webkit
  * 3) https://stackoverflow.com/questions/38243490/reducing-cpu-usage-of-navigator-webkitgetusermedia-electron-desktopcapturer

### Testing

These posts discuss aspects related to application testing, often seeking clarification regarding test frameworks and tools. *'Mocha test setup to run two tests who require same beforeEach setup'* is an example. Analyzing the questions of this topic, we noticed that the main reason why developers experience testing-related difficulties is that commonly used testing frameworks and tools are often not compatible with desktop web app frameworks. Instead, ad-hoc tools or wrappers for existing ones must be utilized in their place. Multiple examples are found in Stack Overflow questions: packages such as *spectron*, *electron-chromedriver* and *nw-chromedriver* provide wrappers for the popular ChromeDriver automated testing tool; whereas, *nw-test-runner* and *electron-mocha* wrap around the Mocha testing framework. 

**Considerations:**
  * Ad-hoc wrappers are required to make existing testing frameworks and tools usable for desktop web application development.
  
**Examples:**
  * 1) https://stackoverflow.com/questions/43529350/why-wont-these-chai-tests-fail
  * 2) https://stackoverflow.com/questions/42551498/electron-run-end-to-end-tests-with-protractor
  * 3) https://stackoverflow.com/questions/42490011/mocha-test-setup-to-run-two-tests-who-require-same-beforeeach-setup

### User interface

Questions in this topic discuss aspects related to the application user interface. Differently from the Page contents topic, questions in this topic deal more closely with aspects that are only found in desktop applications, such as the organization of the menu bar (*'Electron OSX application menu - how to add custom File menu?'*) and the organization of app windows (*'Node-Webkit (nwjs) How to align window to the right?'*).

**Considerations:**
  * Customizing the app user-inteface to provide an user experience that is very similar to the one of native applications is important for desktop application developers. At the same time it currently requires a considerable effort. 

**Examples:**
  * 1) https://stackoverflow.com/questions/28853289/style-system-tray-with-node-webkit-application
  * 2) https://stackoverflow.com/questions/31790535/get-and-set-correct-window-position-with-node-js
  * 3) https://stackoverflow.com/questions/38441935/electron-app-turn-off-on-screen-keyboard-windows-10-tablet

## GitHub Topics

In the following, we briefly describe the relevant topics uniquely found in the GitHub dataset in detail and provide illustrative examples from selected GitHub issue reports.

### Account, Cryptocurrencies, and Messaging

Issues in these topics discuss complications that occur when using app functionalities associated with the respective arguments, e.g., login, profile update, sending/receiving cryptocurrencies, chats and private messages. Illustrative examples are the issue titled *'Invalid auto-login after login attempt with no data'* from the repository *simplenote-electron* and the issue *'Batch sending LSK to wallets'* from the repository *lisk-desktop*.

**Examples:**
  * 1) https://github.com/Foundry376/Mailspring/issues/1313
  * 2) https://github.com/LiskHQ/lisk-desktop/issues/978
  * 3) https://github.com/Automattic/simplenote-electron/issues/212

### Feature request

Issues in this topic suggest new application features or require improvements to existing ones. An issue of this kind is the following, taken from the app *Boostnote*: *'Add a lock button to the Preview mode'*. This kind of issue is frequently found in GitHub repositories..

**Examples:**
  * 1) https://github.com/Atraci/Atraci/issues/187
  * 2) https://github.com/Automattic/simplenote-electron/issues/1009
  * 3) https://github.com/Kong/insomnia/issues/266

### Input

This topics encompasses those issues that describe a problem tied to the application input methods. An instance of this kind of issue is *'Selecting text using the keyboard automatically copies it'* from the repository *extraterm*.

**Examples:**
  * 1) https://github.com/Eugeny/terminus/issues/768
  * 2) https://github.com/OpenBazaar/openbazaar-desktop/issues/1098
  * 3) https://github.com/Soundnode/soundnode-app/issues/705

### Text manipulation

Issues related to this topic describe problems related to the manipulation of on-screen text, e.g., display, selection and highlighting. An example is the issue *'Add Markdown fenced code blocks (Syntax highlighting)'* from the repository *beakerbrowser*.

**Examples:**
  * 1) https://github.com/BoostIO/Boostnote/issues/1490
  * 2) https://github.com/Kong/insomnia/issues/1712
  * 3) https://github.com/Kong/insomnia/issues/412
