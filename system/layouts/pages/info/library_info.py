import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

authors = {
"Aldous Leonard Huxley": {"description":
    html.Div([
        dbc.Row([
            dbc.Col(html.Img(src="./assets/images/authors/aldous_leonard_huxley_.jpg", className="author-description-img"), width="auto", className="author-description-img-col"),
            dbc.Col([
                html.P("""Aldous Leonard Huxley"""),
                html.P("""26 July 1894 - 22 November 1963""")
            ], className="author-description-header", width="auto")
        ]),
        html.Hr(),
        html.Div([
            html.P("""Aldous Leonard Huxley was an English writer and philosopher."""),
            html.P("""He wrote nearly 50 books—both novels and non-fiction works—as well as wide-ranging essays, narratives, and poems."""),
            html.P("""By the end of his life, Huxley was widely acknowledged as one of the foremost intellectuals of his time."""),
            html.P("""He was nominated for the Nobel Prize in Literature nine 
            times and was elected Companion of Literature by the Royal Society of Literature in 1962."""),
            html.P("The Sherlock Holmes stories are considered milestones in the field of crime fiction."),
            html.P("""Huxley was a pacifist."""),
            html.P("""In his most famous novel Brave New World (1932) and his final novel Island (1962), 
            he presented his vision of dystopia and utopia, respectively.""")
        ], className="author-description-body")
    ])},

"Arthur Ignatius Conan Doyle": {"description":
    html.Div([
        dbc.Row([
            dbc.Col(html.Img(src="./assets/images/authors/arthur_ignatius_conan_doyle.jpg", className="author-description-img"), width="auto", className="author-description-img-col"),
            dbc.Col([
                html.P("""Sir Arthur Ignatius Conan Doyle"""),
                html.P("""22 May 1859 – 7 July 1930""")
            ], className="author-description-header", width="auto")
        ]),
        html.Hr(),
        html.Div([
            html.P("""Conan Doyle was a British writer and physician."""),
            html.P("""He created the character Sherlock Holmes in 1887 for A Study in Scarlet, 
            the first of four novels and fifty-six short stories about Holmes and Dr. Watson."""),
            html.P("""The Sherlock Holmes stories are considered milestones in the field of crime fiction."""),
            html.P("""Doyle was a prolific writer; other than Holmes stories, his works include fantasy 
            and science fiction stories about Professor Challenger and humorous stories about 
            the Napoleonic soldier Brigadier Gerard, as well as plays, romances, poetry, 
            non-fiction and historical novels."""),
            html.P("""One of Doyle's early short stories, "J. Habakuk Jephson's Statement" (1884), 
            helped to popularise the mystery of the Mary Celeste.""")
        ], className="author-description-body")
    ])},

"Clinton Richard Dawkins": {"description":
    html.Div([
        dbc.Row([
            dbc.Col(html.Img(src="./assets/images/authors/clinton_richard_dawkins_.jpg", className="author-description-img"), width="auto", className="author-description-img-col"),
            dbc.Col([
                html.P("""Clinton Richard Dawkins"""),
                html.P("""26 March 1941""")
            ], className="author-description-header", width="auto")
        ]),
        html.Hr(),
        html.Div([
            html.P("""Richard Dawkins FRS FRSL is a British ethologist, evolutionary biologist, and author."""),
            html.P("""He is an emeritus fellow of New College, Oxford, and was the University of Oxford's 
            Professor for Public Understanding of Science from 1995 until 2008."""),
            html.P("""An atheist, he is well known for his criticism of creationism and intelligent design."""),
            html.P("""Dawkins first came to prominence with his 1976 book The Selfish Gene, which popularised 
            the gene-centred view of evolution and introduced the term meme. With his book The Extended Phenotype 
            (1982), he introduced into evolutionary biology the influential concept that the phenotypic effects 
            of a gene are not necessarily limited to an organism's body, but can stretch far into the environment.
            In 2006, he founded the Richard Dawkins Foundation for Reason and Science."""),
            html.P("""In The Blind Watchmaker (1986), Dawkins argues against the watchmaker analogy, an argument 
            for the existence of a supernatural creator based upon the complexity of living organisms. Instead, 
            he describes evolutionary processes as analogous to a blind watchmaker, in that reproduction, mutation,
            and selection are unguided by any designer. In The God Delusion (2006), Dawkins contends that a supernatural
            creator almost certainly does not exist and that religious faith is a delusion. Dawkins' atheist stances 
            have sometimes attracted controversy."""),
            html.P("""Dawkins has been awarded academic and writing awards, and he makes television, radio, and internet
            appearances, predominantly discussing his books, atheism, and his ideas and opinions as a public intellectual""")
        ], className="author-description-body")
    ])},
}