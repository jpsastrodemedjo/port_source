title: Induction    
author: JP Sastrodemedjo\
Date: 04/04/2020  
Category: Trainee Blog  
Tags: python, markdown, pelican
Slug: Induction

### Week 1 Blog

1. Learned how to use **Git**
    * tracking
    * adding to the staging area
    * committing changes
    * adding files to remote repositories (github)
    * branching and merging)
2. Completed **Fundamental of Medical Ethics** course
3. Completed **IAEA Safety and Quality in RT** course
4. Read SLRON **Local Rules**, Policies & Procedures etc.
5. Learned how to generate a static site with pelican & markdown (in vscode)
6. This is how syntax highlighting works, indent and 3 colons with the name of the language (python3)

        :::python3  
        x = ("hello")   
        print(x)

7. To deploy a static website to Github pages

    While in the *blog/output* folder run the following git commands in order to push files to the *username.github.io* repository.

    ```git init```  
    ```git remote add origin https://github.com/username/username.github.io```  
    ```git add .```  
    ```git commit -m "initial commit" ```   
    ```git push -u origin master```

    Next, navigate to the *blog/source* folder run the following git commands in order to push our files to the blog_source repository:

    ```git init```  
    ```git remote add origin https://github.com/username/port_blog```   
    ```git add .```  
    ```git commit -m "initial commit"```    
    ```git push -u origin master``` 

    After running both sequences of Git commands we should be able to see our files loaded into their respective repositories on Github. To view the website type [https://jpsastrodemedjo.github.io](https://jpsastrodemedjo.github.io) into your web browser.

    [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

### Week 2 To-do list

- Read HSE Polices + Procedures
- Python Session with Pat (Wed)
- Radiation Safety Procedures Q+A (Thurs)
- Basic Interactions oral exam (Fri)