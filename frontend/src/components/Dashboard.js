import React from 'react';
import { useNavigate } from 'react-router-dom';


function Dashboard() {

  const navigate = useNavigate();                                             

  return (
      <div className="section">
        <h1 className="title has-text-centered">Dashboard</h1>
        
        
      </div>
    );
}

export default Dashboard;


/*
Przykładowy wygląd dashboardu:

-----------------------------------------------
| Gracz: [Imię Gracza]       Poziom: [Poziom] |
| HP: [75/100]               Lokacja: [Wioska] |
| Punkty Akcji: [2]                            |
-----------------------------------------------
|                                               |
| [Aktualna Lokacja / Tekst fabularny]         |
|                                               |
| “Zbliżasz się do tajemniczej jaskini. Co robisz?”|
|                                               |
| >> [Wprowadź akcję: Zbadaj jaskinię]           |
|                                               |
-----------------------------------------------
| Chat:                                         |
|                                               |
| Gracz 1: “Pomóż mi, atakujemy smoka!”         |
| Gracz 2: “Daj mi chwilę!”                     |
|                                               |
| [Pole tekstowe na wiadomości]                 |
| >> [Wpisz wiadomość]                          |
| [Przycisk: Wyślij]                            |
-----------------------------------------------
| Przyciski akcji: [Atakuj] [Zbadaj] [Rozmawiaj] |

 */