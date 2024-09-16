import React from 'react';
import { Link } from 'react-router-dom';
import styles from '../styles/Header.module.css';

const Header: React.FC = () => {
    return (
        <header className={styles.header}>
            <h1 className={styles.title}>TechBlog</h1>
            <nav className={styles.nav}>
                <Link to="/">Início</Link>
                <Link to="/posts">Posts</Link>
                <Link to="/about">Sobre</Link>
                <Link to="/contact">Contato</Link>
            </nav>
        </header>
    );
};

export default Header;
