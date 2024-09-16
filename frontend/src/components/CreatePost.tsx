import React, { useState } from 'react';
import axios from 'axios';

const CreatePost: React.FC = () => {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [error, setError] = useState('');

    const handleCreatePost = async () => {
        const token = localStorage.getItem('token');
        if (!token) {
            setError('Você precisa estar logado para criar um post');
            return;
        }

        try {
            const response = await axios.post('http://localhost:5000/admin/posts', 
                { title, content },
                { headers: { Authorization: `Bearer ${token}` } }
            );
            setTitle('');
            setContent('');
            setError('');
        } catch (err) {
            setError('Erro ao criar post');
        }
    };

    return (
        <div>
            <h2>Criar Post</h2>
            <input
                type="text"
                placeholder="Título"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
            />
            <textarea
                placeholder="Conteúdo"
                value={content}
                onChange={(e) => setContent(e.target.value)}
            />
            <button onClick={handleCreatePost}>Criar Post</button>
            {error && <p>{error}</p>}
        </div>
    );
};

export default CreatePost;
