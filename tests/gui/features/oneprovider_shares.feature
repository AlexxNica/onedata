Feature: Oneprovider Share view
  Various operations on Share view

  Background:
    Given user opened browser window
    And user of browser opened Onezone URL
    And user of browser clicked on the "plgrid" login button
    And user of browser clicked on the "user1" link
    And user of browser expanded the "go to your files" Onezone sidebar panel
    And user of browser clicked on the "p1" provider in Onezone providers sidebar panel
    And user of browser clicked on the "Go to your files" button in provider popup
    And user of browser seen that Oneprovider session has started


  Scenario: User creates share and see share icon on shared directory (presses ENTER after typing share name)
    When user of browser uses spaces select to change data space to "space1"
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 directory has appeared in file list

    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Share element"

    And user of browser sees that "Share the directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "share1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees an info notify with text matching to: Share created sucessfully
    And user of browser sees that modal has disappeared

    And user of browser sees that "Share summary" modal has appeared
    And user of browser clicks "Close" confirmation button in displayed modal
    And user of browser sees that modal has disappeared
    And user of browser sees dir1 as shared-directory in file list

    # TODO rm after integrating with swagger
    Then user of browser uses spaces select to change data space to "Small space"
    And user of browser uses spaces select to change data space to "space1"
    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Remove element"
    And user of browser sees that "Remove files" modal has appeared
    And user of browser clicks "OK" confirmation button in displayed modal
    And user of browser sees an success notify with text matching to: .*removed.*
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 shared-directory has disappeared from file list


  Scenario: User creates share and see share icon on shared directory (clicks CREATE confirmation button after typing share name)
    When user of browser uses spaces select to change data space to "space1"
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 directory has appeared in file list

    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Share element"

    And user of browser sees that "Share the directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "share1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees an info notify with text matching to: Share created sucessfully
    And user of browser sees that modal has disappeared

    And user of browser sees that "Share summary" modal has appeared
    And user of browser clicks "Close" confirmation button in displayed modal
    And user of browser sees that modal has disappeared
    And user of browser sees dir1 as shared-directory in file list

    # TODO rm after integrating with swagger
    Then user of browser uses spaces select to change data space to "Small space"
    And user of browser uses spaces select to change data space to "space1"
    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Remove element"
    And user of browser sees that "Remove files" modal has appeared
    And user of browser clicks "OK" confirmation button in displayed modal
    And user of browser sees an success notify with text matching to: .*removed.*
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 shared-directory has disappeared from file list


  Scenario: Opening shares index view after removing shared dir
    When user of browser uses spaces select to change data space to "space1"
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 directory has appeared in file list

    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Share element"

    And user of browser sees that "Share the directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "share1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees an info notify with text matching to: Share created sucessfully
    And user of browser sees that modal has disappeared

    And user of browser sees that "Share summary" modal has appeared
    And user of browser clicks "Open the share" confirmation button in displayed modal
    And user of browser sees that url matches https?://[^/]*/#/onedata/shares/.*
    And user of browser sees that share named "share1" has appeared in the shared list
    And user of browser clicks on the "data" tab in main menu sidebar

    And user of browser uses spaces select to change data space to "space1"
    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Remove element"
    And user of browser sees that "Remove files" modal has appeared
    And user of browser clicks "OK" confirmation button in displayed modal
    And user of browser sees an success notify with text matching to: .*removed.*
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 shared-directory has disappeared from file list

    And user of browser clicks on the "shared" tab in main menu sidebar
    And user of browser does not see any share info


  Scenario: User fails to share already shared directory
    When user of browser uses spaces select to change data space to "space1"
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 directory has appeared in file list

    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Share element"

    And user of browser sees that "Share the directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "share1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees an info notify with text matching to: Share created sucessfully
    And user of browser sees that modal has disappeared

    And user of browser sees that "Share summary" modal has appeared
    And user of browser clicks "Close" confirmation button in displayed modal
    And user of browser sees that modal has disappeared
    And user of browser sees dir1 as shared-directory in file list

    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Share element"
    And user of browser sees that "Share summary" modal has appeared
    And user of browser clicks "Close" confirmation button in displayed modal
    And user of browser sees that modal has disappeared

    # TODO rm after integrating with swagger
    Then user of browser uses spaces select to change data space to "Small space"
    And user of browser uses spaces select to change data space to "space1"
    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Remove element"
    And user of browser sees that "Remove files" modal has appeared
    And user of browser clicks "OK" confirmation button in displayed modal
    And user of browser sees an success notify with text matching to: .*removed.*
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 shared-directory has disappeared from file list


  Scenario: User creates share and sees it's info
    When user of browser uses spaces select to change data space to "space1"
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 directory has appeared in file list

    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Share element"

    And user of browser sees that "Share the directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "share1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees an info notify with text matching to: Share created sucessfully
    And user of browser sees that modal has disappeared

    And user of browser sees that "Share summary" modal has appeared
    And user of browser clicks "Open the share" confirmation button in displayed modal
    And user of browser sees that url matches https?://[^/]*/#/onedata/shares/.*
    And user of browser sees that share named "share1" has appeared in the shared list

    And user of browser selects share named "share1" from the shared list
    And user of browser sees that selected share is named "share1"
    And user of browser sees that absolute share path is space1/dir1

    # TODO rm after integrating with swagger
    Then user of browser clicks on the "data" tab in main menu sidebar
    And user of browser uses spaces select to change data space to "Small space"
    And user of browser uses spaces select to change data space to "space1"
    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Remove element"
    And user of browser sees that "Remove files" modal has appeared
    And user of browser clicks "OK" confirmation button in displayed modal
    And user of browser sees an success notify with text matching to: .*removed.*
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 shared-directory has disappeared from file list


  Scenario: User sees new files after adding them to shared directory
    When user of browser uses spaces select to change data space to "space1"
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 directory has appeared in file list

    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Share element"

    And user of browser sees that "Share the directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "share1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees an info notify with text matching to: Share created sucessfully
    And user of browser sees that modal has disappeared

    And user of browser sees that "Share summary" modal has appeared
    And user of browser clicks "Open the share" confirmation button in displayed modal
    And user of browser sees that url matches https?://[^/]*/#/onedata/shares/.*
    And user of browser sees that share named "share1" has appeared in the shared list
    And user of browser clicks on the "data" tab in main menu sidebar

    And user of browser uses spaces select to change data space to "space1"
    And user of browser double clicks on directory dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Create file"
    And user of browser sees that "New file" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "file3" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that file3 file has appeared in file list

    And user of browser clicks on the "shared" tab in main menu sidebar
    And user of browser selects share named "share1" from the shared list
    And user of browser sees that current working directory is share1
    And user of browser double clicks on directory dir1 from files list
    And user of browser sees that current working directory is share1/dir1
    And user of browser sees file3 as file in file list

    # TODO rm after integrating with swagger
    Then user of browser clicks on the "data" tab in main menu sidebar
    And user of browser uses spaces select to change data space to "Small space"
    And user of browser uses spaces select to change data space to "space1"
    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Remove element"
    And user of browser sees that "Remove files" modal has appeared
    And user of browser clicks "OK" confirmation button in displayed modal
    And user of browser sees an success notify with text matching to: .*removed.*
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 shared-directory has disappeared from file list


  Scenario: User opens the share using shared icon
    When user of browser uses spaces select to change data space to "space1"
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 directory has appeared in file list

    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Share element"

    And user of browser sees that "Share the directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "share1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees an info notify with text matching to: Share created sucessfully
    And user of browser sees that modal has disappeared

    And user of browser sees that "Share summary" modal has appeared
    And user of browser clicks "Close" confirmation button in displayed modal
    And user of browser sees that modal has disappeared

    And user of browser clicks on share icon in tools column for dir1 directory
    And user of browser sees that "Share summary" modal has appeared
    And user of browser clicks "Open the share" confirmation button in displayed modal
    And user of browser sees that url matches https?://[^/]*/#/onedata/shares/.*
    And user of browser sees that share named "share1" has appeared in the shared list
    And user of browser selects share named "share1" from the shared list
    And user of browser sees that selected share is named "share1"
    And user of browser sees that absolute share path is space1/dir1

    # TODO rm after integrating with swagger
    Then user of browser clicks on the "data" tab in main menu sidebar
    And user of browser uses spaces select to change data space to "Small space"
    And user of browser uses spaces select to change data space to "space1"
    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Remove element"
    And user of browser sees that "Remove files" modal has appeared
    And user of browser clicks "OK" confirmation button in displayed modal
    And user of browser sees an success notify with text matching to: .*removed.*
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 shared-directory has disappeared from file list


  Scenario: User can jump to outer directory from inner one
    When user of browser uses spaces select to change data space to "space1"
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 directory has appeared in file list

    And user of browser double clicks on directory dir1 from files list
    And user of browser uses upload button in toolbar to upload file "20B-0.txt" to current dir
    And user of browser sees an info notify with text matching to: .*20B-0\.txt.*uploaded successfully.*
    And user of browser sees that 20B-0.txt file has appeared in file list
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir2" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir2 directory has appeared in file list

    And user of browser double clicks on directory dir2 from files list
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir3" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir3 directory has appeared in file list

    And user of browser uses spaces select to change data space to "Small space"
    And user of browser uses spaces select to change data space to "space1"
    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Share element"

    And user of browser sees that "Share the directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "share1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees an info notify with text matching to: Share created sucessfully
    And user of browser sees that modal has disappeared

    And user of browser sees that "Share summary" modal has appeared
    And user of browser clicks "Open the share" confirmation button in displayed modal
    And user of browser sees that url matches https?://[^/]*/#/onedata/shares/.*
    And user of browser sees that share named "share1" has appeared in the shared list

    And user of browser selects share named "share1" from the shared list
    And user of browser sees that selected share is named "share1"
    And user of browser sees that absolute share path is space1/dir1
    And user of browser sees that current working directory is share1
    And user of browser double clicks on directory dir1 from files list
    And user of browser sees that current working directory is share1/dir1
    And user of browser double clicks on directory dir2 from files list
    And user of browser sees that current working directory is share1/dir1/dir2
    And user of browser double clicks on directory dir3 from files list
    And user of browser sees that current working directory is share1/dir1/dir2/dir3
    And user of browser clicks on share1/dir1 using breadcrumbs from file browser
    And user of browser sees that current working directory is share1/dir1
    And user of browser sees that dir2 directory has appeared in file list
    And user of browser sees that 20B-0.txt file has appeared in file list

    # TODO rm after integrating with swagger
    Then user of browser clicks on the "data" tab in main menu sidebar
    And user of browser uses spaces select to change data space to "Small space"
    And user of browser uses spaces select to change data space to "space1"
    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Remove element"
    And user of browser sees that "Remove files" modal has appeared
    And user of browser clicks "OK" confirmation button in displayed modal
    And user of browser sees an success notify with text matching to: .*removed.*
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 shared-directory has disappeared from file list


  Scenario: User does not see files after removing them from shared directory
    When user of browser uses spaces select to change data space to "space1"
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 directory has appeared in file list

    And user of browser double clicks on directory dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Create file"
    And user of browser sees that "New file" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "file3" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that file3 file has appeared in file list

    And user of browser uses spaces select to change data space to "Small space"
    And user of browser uses spaces select to change data space to "space1"
    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Share element"

    And user of browser sees that "Share the directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "share1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees an info notify with text matching to: Share created sucessfully
    And user of browser sees that modal has disappeared

    And user of browser sees that "Share summary" modal has appeared
    And user of browser clicks "Open the share" confirmation button in displayed modal
    And user of browser sees that url matches https?://[^/]*/#/onedata/shares/.*
    And user of browser sees that share named "share1" has appeared in the shared list
    And user of browser selects share named "share1" from the shared list

    And user of browser sees that current working directory is share1
    And user of browser double clicks on directory dir1 from files list
    And user of browser sees that current working directory is share1/dir1
    And user of browser sees that file3 file has appeared in file list

    And user of browser clicks on the "data" tab in main menu sidebar
    And user of browser uses spaces select to change data space to "space1"
    And user of browser double clicks on directory dir1 from files list

    And user of browser selects file3 from files list
    And user of browser clicks the button from top menu bar with tooltip "Remove element"
    And user of browser sees that "Remove files" modal has appeared
    And user of browser clicks "OK" confirmation button in displayed modal
    And user of browser sees an success notify with text matching to: .*removed.*
    And user of browser sees that modal has disappeared
    And user of browser sees that file3 file has disappeared from file list

    And user of browser clicks on the "shared" tab in main menu sidebar
    And user of browser selects share named "share1" from the shared list
    And user of browser sees that current working directory is share1
    And user of browser double clicks on directory dir1 from files list
    And user of browser sees that current working directory is share1/dir1
    And user of browser sees that file3 file has disappeared from file list

    # TODO rm after integrating with swagger
    Then user of browser clicks on the "data" tab in main menu sidebar
    And user of browser uses spaces select to change data space to "Small space"
    And user of browser uses spaces select to change data space to "space1"
    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Remove element"
    And user of browser sees that "Remove files" modal has appeared
    And user of browser clicks "OK" confirmation button in displayed modal
    And user of browser sees an success notify with text matching to: .*removed.*
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 shared-directory has disappeared from file list


  Scenario: User can jump to outer directory from inner one
    When user of browser uses spaces select to change data space to "space1"
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 directory has appeared in file list

    And user of browser double clicks on directory dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir2" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir2 directory has appeared in file list

    And user of browser double clicks on directory dir2 from files list
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir3" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir3 directory has appeared in file list

    And user of browser uses spaces select to change data space to "Small space"
    And user of browser uses spaces select to change data space to "space1"
    And user of browser double clicks on directory dir1 from files list
    And user of browser selects dir2 from files list
    And user of browser clicks the button from top menu bar with tooltip "Share element"

    And user of browser sees that "Share the directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "share1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees an info notify with text matching to: Share created sucessfully
    And user of browser sees that modal has disappeared

    And user of browser sees that "Share summary" modal has appeared
    And user of browser clicks "Open the share" confirmation button in displayed modal
    And user of browser sees that url matches https?://[^/]*/#/onedata/shares/.*
    And user of browser sees that share named "share1" has appeared in the shared list
    And user of browser selects share named "share1" from the shared list
    And user of browser sees that selected share is named "share1"
    And user of browser sees that absolute share path is space1/dir1/dir2

    And user of browser clicks on the "data" tab in main menu sidebar
    And user of browser uses spaces select to change data space to "Small space"
    And user of browser uses spaces select to change data space to "space1"
    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Remove element"
    And user of browser sees that "Remove files" modal has appeared
    And user of browser clicks "OK" confirmation button in displayed modal
    And user of browser sees an success notify with text matching to: .*removed.*
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 directory has disappeared from file list

    And user of browser clicks on the "shared" tab in main menu sidebar
    And user of browser refreshes site
    Then user of browser sees that share named "share1" has disappeared from the shares list


  Scenario: User can jump to data tab by clicking on dir in breadcrumbs from shared tab
    When user of browser uses spaces select to change data space to "space1"
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 directory has appeared in file list

    And user of browser double clicks on directory dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir2" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir2 directory has appeared in file list

    And user of browser double clicks on directory dir2 from files list
    And user of browser clicks the button from top menu bar with tooltip "Create directory"
    And user of browser sees that "New directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "dir3" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees that modal has disappeared
    And user of browser sees that dir3 directory has appeared in file list

    And user of browser uses spaces select to change data space to "Small space"
    And user of browser uses spaces select to change data space to "space1"
    And user of browser double clicks on directory dir1 from files list
    And user of browser selects dir2 from files list
    And user of browser clicks the button from top menu bar with tooltip "Share element"

    And user of browser sees that "Share the directory" modal has appeared
    And user of browser clicks on input box in active modal
    And user of browser types "share1" on keyboard
    And user of browser presses enter on keyboard
    And user of browser sees an info notify with text matching to: Share created sucessfully
    And user of browser sees that modal has disappeared

    And user of browser sees that "Share summary" modal has appeared
    And user of browser clicks "Open the share" confirmation button in displayed modal
    And user of browser sees that url matches https?://[^/]*/#/onedata/shares/.*
    And user of browser sees that share named "share1" has appeared in the shared list

    And user of browser selects share named "share1" from the shared list
    And user of browser sees that selected share is named "share1"
    And user of browser sees that absolute share path is space1/dir1/dir2
    And user of browser sees that current working directory is share1
    And user of browser double clicks on directory dir2 from files list
    And user of browser sees that current working directory is share1/dir2
    And user of browser sees dir3 as directory in file list

    And user of browser clicks on space1/dir1 using breadcrumbs from share info header
    And user of browser sees that url matches https?://[^/]*/#/onedata/data/.*
    And user of browser sees that current working directory displayed in sidebar list is space1/dir1

    # TODO rm after integrating with swagger
    Then user of browser clicks on the "data" tab in main menu sidebar
    And user of browser uses spaces select to change data space to "Small space"
    And user of browser uses spaces select to change data space to "space1"
    And user of browser selects dir1 from files list
    And user of browser clicks the button from top menu bar with tooltip "Remove element"
    And user of browser sees that "Remove files" modal has appeared
    And user of browser clicks "OK" confirmation button in displayed modal
    And user of browser sees an success notify with text matching to: .*removed.*
    And user of browser sees that modal has disappeared
    And user of browser sees that dir1 shared-directory has disappeared from file list
