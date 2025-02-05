import { useState, useEffect, useRef, useCallback } from "react";

const useChat = (roomId) => {
  const [chatMessages, setChatMessages] = useState([{ id: 1, text: "Rozpocznij czat!", user: "System" }]);
  const [username, setUsername] = useState(localStorage.getItem("username") || "Anonim");
  const [isTokenValid, setIsTokenValid] = useState(null);
  const socket = useRef(null);
  const receivedMessages = useRef(new Set());
  const accessToken = localStorage.getItem("access");

  useEffect(() => {
    setIsTokenValid(!!accessToken);
    setUsername(localStorage.getItem("username") || "Anonim");
  }, []);

  const connectWebSocket = useCallback(() => {
    if (!roomId) return console.error("❌ Brak roomId. WebSocket nie może się połączyć.");

    if (socket.current) {
      socket.current.close();
    }

    const wsUrl = `ws://localhost:8000/ws/chat/${roomId}/?token=${accessToken}`;
    socket.current = new WebSocket(wsUrl);

    socket.current.onopen = () => console.log(`✅ WebSocket połączony z pokojem: ${roomId}`);
    socket.current.onerror = (error) => console.error("❌ Błąd WebSocket", error);
    socket.current.onmessage = (e) => handleWebSocketMessage(e);
    socket.current.onclose = () => {
      console.warn("⚠️ WebSocket zamknięty. Ponowne łączenie za 3 sekundy...");
      socket.current = null;
      setTimeout(connectWebSocket, 3000);
    };
  }, [accessToken, roomId]);

  const handleWebSocketMessage = (e) => {
    const data = JSON.parse(e.data);
    if (receivedMessages.current.has(data.message_id)) return;
    receivedMessages.current.add(data.message_id);

    const sender = data.sender || "Nieznajomy";
    setChatMessages((prev) => [...prev, { id: prev.length + 1, text: data.message, user: sender }]);
  };

  useEffect(() => {
    if (isTokenValid) connectWebSocket();
    return () => socket.current?.close();
  }, [isTokenValid, connectWebSocket]);

  const sendMessage = (message) => {
    if (!socket.current || socket.current.readyState !== WebSocket.OPEN) return;
    socket.current.send(JSON.stringify({ message, sender: username }));
  };

  return { chatMessages, sendMessage, isTokenValid };
};

export default useChat;
