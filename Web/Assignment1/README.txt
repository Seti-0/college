This is a dummy website about a (fictional!) game engine.
Please note that the text content is nonsense! 
None of this exists, and the games in the showcase are certainly not from a single engine.

Regarding CSS - I ended up writing one CSS file only. It was shorter
than I expected it to be, especially after I reorganized some things into 
classes.

I'm also using the "reset.css" from http://meyerweb.com/eric/tools/css/reset/

REQUIRED ELEMENTS:

    > The home page is called "index.html". The gallery page is called "showcase.html", accessible by clicking
        "Showcase" in the nav bar at the top. The remaining three pages are "Features", "Getting Started" and "News"

    > There are links to internal and external pages on the intro page:
    
        - "Getting Started" links to the internal page of the same name
        
        - "contributor's guide" links to an external github wiki page
        
    > The navigation bar is there, with 5 links, one to each internal page.
    
    > A table can be found on the "Getting Started" (third, blue) page, displaying version information.
    
    > Some unordered lists can be found on the "Features" (second, pink) page.
    
    > A local video can be found on the "News" (last, green) page.
    
    > For CSS3 specific elements:
    
        - "border-radius" is used widely (for eg, main.css: line 38)
        
        - "display: flex" and "flex-wrap" can be found at main.css: lines 122 & 123
        
        - "display: inline-grid" and the various grid properties are used to lay out the "Features" and "News" pages. They can be found at main.css: lines 177 & 321
        
    > For HTML specific elements:
    
        - Semantic elements are used extensively. To name 4: "nav", "section", "figure", "figcaption" all can be found on index.html
        
    > Lots of inline elements are used, such as the elements of the nav bar and the elements of the image gallery. Block elements
        are also used: the "main container" div exists on all pages except for the home page and is a block element.
        
        
RESPONSIVENESS:

    > The site was originally designed to be naturally responsive, without the use of media queries.
    
        - That is, resizing the browser causes pages to collapse in a user friendly way for the most part
        
        - I notice that while the page responds fine to resizing, it doesn't seem to respond at all
            to google chrome's built in device simulator. I don't know why this is.
        
    > % maxsize, "inline-block" and the "flex-box" where all important in this goal
    
    > I made a mistake in using a grid layout in the Features page, I think. It doesn't respond well to 
        very small sizes where the image is a big as the screen.
        
        
ATTRIBUTION:

    > logo.svg (the planet logo) was adapted from an icon created by Freepik (https://www.freepik.com/) found on Flaticon (https://www.flaticon.com/).

    > The remaining svg images were created in inkscape by me.

    > The video is from youtube, and created by EpicGames.

    > Each image in the showcase is from a game whose site can be accessed by clicking on the image. These are:
    
        - dust.jpg: https://www.ironhidegames.com/Games/kingdom-rush-origins
        
        - kingdom.jpg: https://fractalsoftworks.com/
        
        - magick.jpg: http://www.zachtronics.com/shenzhen-io/
        
        - ring.jpg: http://trine2.com/site/
        
        - shenzhen.png: http://www.tastystewdios.com/
        
        - starsector.png: http://ringrunner.net/
        
        - trine.jpg: http://www.elysiantail.com/]
        
    > The inspiration for the actual website actually came from http://biomedicalblockchain.org/
    
        - Obviously it changed a lot. The "design" folder contains svgs used in coming up with it.
    
    