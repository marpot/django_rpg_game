#!/bin/bash

echo "🔄 Synchronizacja zmiennych środowiskowych REACT_APP_..."

> frontend/.env.development
grep '^REACT_APP_' .env.development > frontend/.env.development

echo "✅ Zmienna środowiskowa REACT_APP_ została zapisana do frontend/.env.development"
