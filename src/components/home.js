import React from 'react'
import { graphql, StaticQuery } from 'gatsby'

import Layout from './layout'
import { Link } from './link'
import { Logo } from './logo'

import classes from '../styles/index.module.sass'

export default ({ lang = 'en' }) => {
    return (
        <StaticQuery
            query={query}
            render={data => {
                const chapters = data.allMarkdownRemark.edges
                    .filter(({ node }) => node.fields.lang === lang)
                    .map(({ node }) => ({
                        slug: node.fields.slug,
                        title: node.frontmatter.title,
                        description: node.frontmatter.description,
                    }))
                return (
                    <Layout isHome lang={lang}>
                        <Logo lang={lang} className={classes.logo} />
                        <section>
                                <h1 className={classes.subtitle}><center>DSCI 511 - Programming in Python for Data Science</center></h1>
                                    <div className={classes.introduction}>
                                        <p>
                                        <center> Welcome to DSCI 511!  This course is part of UBC's Mid-Careers Learning program. In this course we hope to introduce you to basic programming in Python. You will leave this course with an overview of iteration and flow control as well as data types relevant to data exploration and analysis. You will learn about pre-existing libraries, numerical data types with Numpy and tabular data with Pandas. No course would be complete without knowing how to wrangle your data. With the help from Pandas, you will learn how to convert data from the form in which it is collected to the form needed for analysis. 
                                        </center>
                                        </p>
                                        <p>
                                        <strong>Course prerequisites:</strong> None
                        </p>
                             </div>
                    </section>
                        {chapters.map(({ slug, title, description }) => (
                            <section key={slug} className={classes.chapter}>
                                <h2 className={classes.chapterTitle}>
                                    <Link hidden to={slug}>
                                        {title}
                                    </Link>
                                </h2>
                                <p className={classes.chapterDesc}>
                                    <Link hidden to={slug}>
                                        {description}
                                    </Link>
                                </p>
                            </section>
                        ))}
                    </Layout>
                )
            }}
        />
    )
}

const query = graphql`
    {
        allMarkdownRemark(
            sort: { fields: [frontmatter___title], order: ASC }
            filter: { frontmatter: { type: { eq: "chapter" } } }
        ) {
            edges {
                node {
                    fields {
                        slug
                        lang
                    }
                    frontmatter {
                        title
                        description
                    }
                }
            }
        }
    }
`
