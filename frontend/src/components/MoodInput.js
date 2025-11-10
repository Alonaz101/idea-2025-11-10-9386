// SCRUM-223: React component for mood input
import React, { useState } from 'react';

const MoodInput = ({ onSubmitMood }) => {
  const [mood, setMood] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (mood) {
      onSubmitMood(mood);
      setMood('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="mood-input">Enter your mood:</label>
      <input
        id="mood-input"
        type="text"
        value={mood}
        onChange={(e) => setMood(e.target.value)}
        placeholder="How do you feel?"
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default MoodInput;
