import React from 'react'
import { graphql } from 'gatsby'

import Layout from '../components/layout'
import { Link } from '../components/link'
import Logo from '../../static/logo.svg'

import classes from '../styles/index.module.sass'

export default ({ data }) => {
    const siteMetadata = data.site.siteMetadata
    const chapters = data.allMarkdownRemark.edges.map(({ node }) => ({
        slug: node.fields.slug,
        title: node.frontmatter.title,
        description: node.frontmatter.description,
    }))
    return (
        <Layout isHome>
            <Logo className={classes.logo} aria-label={siteMetadata.title} />

            <section>
                <h1 className={classes.subtitle}> DSCI 511 - Programming in Python for Data Science </h1>
                <div className={classes.introduction}>
                <p>
                <center> Welcome to DSCI 511!  This course is part of UBC's Mid-Careers Learning program. In this course we hope to introduce you to basic programming in Python. You will leave this course with an overview of iteration and flow control as well as 
data types relevant to data exploration and analysis. You will learn about pre-existing
libraries, numerical data types with Numpy and tabular data with Pandas. No course would be complete without knowing how to wrangle your data. With the help from Pandas you will learn how to converting data from the form in which it is collected to the form needed for analysis. 
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
}

export const pageQuery = graphql`
    {
        site {
            siteMetadata {
                title
            }
        }
        allMarkdownRemark(
            sort: { fields: [frontmatter___title], order: ASC }
            filter: { frontmatter: { type: { eq: "chapter" } } }
        ) {
            edges {
                node {
                    fields {
                        slug
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
