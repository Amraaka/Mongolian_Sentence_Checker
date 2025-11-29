'use client'

import React, { useState } from 'react';

export default function Home() {
  const [sentence, setSentence] = useState('');
  const [response, setResponse] = useState<string | null>(null);
  const [isSuccess, setIsSuccess] = useState<boolean | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setResponse(null);
    setIsSuccess(null);
    try {
      const res = await fetch('http://127.0.0.1:5000/check_sentence', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sentence }),
      });
      const data = await res.json();
      setResponse(data.success ? `Success: ${data.sentence}` : data.message);
      setIsSuccess(data.success);
    } catch (err) {
      setResponse('Error: Could not connect to backend.');
      setIsSuccess(false);
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-blue-900 flex flex-col items-center justify-center">
      <div className="text-3xl text-white font-bold text-center mb-8">Өгүүлбэр зүй шалгагч</div>
      <div className="flex items-center justify-center w-full h-full">
        <div className="bg-white rounded-2xl shadow-lg p-8 w-full max-w-4xl" style={{ minHeight: '30vh' }}>
          <form onSubmit={handleSubmit} className="flex flex-col h-full">
            <textarea
              value={sentence}
              onChange={e => setSentence(e.target.value)}
              placeholder="Энд дарж бичнэ үү"
              className="flex-1 resize-none border-none outline-none text-black bg-transparent text-lg p-2"
              style={{ minHeight: '300px' }}
              maxLength={1600}
              required
            />
           
            {/* Bottom info bar */}
            <div className="flex items-center justify-between mt-4 text-gray-600 text-sm">
              <div className="flex gap-8">
                <div>
                  <div>Үгийн тоо</div>
                  <div className="text-xl font-semibold">{sentence.trim() ? sentence.trim().split(/\s+/).length : 0}</div>
                </div>
                <div>
                  <div>Тэмдэгтийн тоо</div>
                  <div className="text-xl font-semibold inline-block">{sentence.length}</div>
                  <span className="ml-1 text-gray-400">/1600</span>
                </div>
              </div>
              <button
                type="submit"
                className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 disabled:opacity-50 font-semibold"
                disabled={loading}
              >
                Алдаа шалгах
              </button>
            </div>
          </form>
          {/* Response message */}
          {response && (
            <div
              className={`absolute left-1/2 -translate-x-1/2 bottom-24 bg-white border px-6 py-3 rounded shadow-lg text-lg font-medium z-10 ${isSuccess === false ? 'border-red-400 text-red-700' : 'border-green-400 text-green-700'}`}
            >
              {response}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}


