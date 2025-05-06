import React, { useEffect, useRef } from 'react';
import * as PIXI from 'pixi.js';

const MedievalBackground: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    if (canvasRef.current) {
      const app = new PIXI.Application({
        width: window.innerWidth,
        height: window.innerHeight,
        backgroundColor: 0x1a1a1a,
        view: canvasRef.current,
        transparent: true
      });

      // Create a medieval-style background
      const background = new PIXI.Graphics();
      background.beginFill(0x1a1a1a);
      background.drawRect(0, 0, app.screen.width, app.screen.height);
      background.endFill();
      app.stage.addChild(background);

      // Add some medieval-style elements
      const stoneTexture = PIXI.Texture.WHITE;
      const stone = new PIXI.Sprite(stoneTexture);
      stone.tint = 0x8B4513; // Brown color
      stone.width = app.screen.width;
      stone.height = app.screen.height;
      app.stage.addChild(stone);

      // Add some medieval-style patterns
      const pattern = new PIXI.Graphics();
      pattern.lineStyle(2, 0x8B4513);
      for (let i = 0; i < 10; i++) {
        const x = Math.random() * app.screen.width;
        const y = Math.random() * app.screen.height;
        pattern.moveTo(x, y);
        pattern.lineTo(x + 50, y + 50);
      }
      app.stage.addChild(pattern);

      // Handle window resize
      const handleResize = () => {
        app.renderer.resize(window.innerWidth, window.innerHeight);
        app.stage.width = window.innerWidth;
        app.stage.height = window.innerHeight;
      };

      window.addEventListener('resize', handleResize);
      handleResize(); // Initial resize

      // Cleanup on unmount
      return () => {
        window.removeEventListener('resize', handleResize);
        app.destroy(true);
      };
    }
  }, []);

  return <canvas ref={canvasRef} />;
};

export default MedievalBackground;