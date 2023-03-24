from core.config import settings
from core.database import engine

import models.__all_models
import asyncio


async def create_tables() -> None:
    
    print('Criando tabelas...')
    
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabelas criadas com sucesso!')
    

if __name__ == '__main__':
    
    asyncio.run(create_tables())