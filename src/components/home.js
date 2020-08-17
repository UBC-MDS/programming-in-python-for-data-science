import React from 'react'
import { graphql, StaticQuery } from 'gatsby'

import Layout from './layout'
import { Link } from './link'
import Logo from '../../static/logo.svg'

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
                        <Logo className={classes.logo} />
                        <section>
                                <h1 className={classes.subtitle}><center>DSCI 011 - Programming in Python for Data Science</center></h1>
                                    <div className={classes.introduction}>
                                        <p>
                                        <center>
                                        Welcome to DSCI 011!
                                        This course is part of ABC's Mid-Careers Learning program
                                        and will teach you how to conduct data analysis in Python.
                                        During the course,
                                        you will work with powerful Python packages made for data-science,
                                        including Pandas for wrangling tabular data,
                                        Altair for interactive data visualization and NumPy for working with numerical data types,
                                        You will also learn about iteration, flow control,
                                        and the data types relevant to data exploration and analysis.
                                        You will leave this course capable of processing raw data
                                        into a format suitable for analysis,
                                        writing your own analysis functions,
                                        and derive data-driven insights via the creation of interactive visualizations
                                        and summary tables.
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
