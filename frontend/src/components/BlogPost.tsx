import React from 'react';
import styles from '../styles/BlogPost.module.css';

type BlogPostProps = {
    title: string;
    content: string;
    date: string;
};

const BlogPost: React.FC<BlogPostProps> = ({ title, content, date }) => {
    return (
        <article className={styles.post}>
            <h2 className={styles.title}>{title}</h2>
            <p className={styles.date}>{date}</p>
            <div className={styles.content} dangerouslySetInnerHTML={{ __html: content }} />
        </article>
    );
};

export default BlogPost;
