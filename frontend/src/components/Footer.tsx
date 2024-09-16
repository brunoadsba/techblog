import React from 'react';
import styles from '../styles/Footer.module.css';

const Footer: React.FC = () => {
    return (
        <footer className={styles.footer}>
            <p>© 2024 TechBlog. Todos os direitos reservados.</p>
        </footer>
    );
};

export default Footer;
