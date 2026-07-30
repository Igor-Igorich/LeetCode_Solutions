import numpy as np
import pandas as pd
import logging
from typing import Dict, Optional
from sklearn.model_selection import train_test_split

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)
logger = logging.getLogger('DataPreprocessor')

def generate_data(n_rows: int=100_000) -> pd.DataFrame:
    '''
    Создание первичного синтетического DataFrame.
    
    Args:
        n_rows: Количество строк в итоговом синтетическом DataFrame
    
    Returns:
        pd.DataFrame: синтетический DataFrame
    
    Raises:
        TypeError: Если переданное количество строк n_rows меньше 1
    '''
    
    logger.info(
        'Создание первичного синтетического DataFrame...'
    )
    
    rng = np.random.default_rng(seed=42)
    
    groups = ["Standard", "Premium", "VIP", "Corporate", "Basic"]
    user_group_data = rng.choice(groups, size=n_rows)
    
    account_balance_data = rng.normal(loc=15000.0, scale=5000.0, size=n_rows)

    nan_mask = rng.random(size=n_rows) < 0.10
    account_balance_data[nan_mask] = np.nan
    
    data = {
        'user_group': user_group_data,
        'account_balance': account_balance_data,
        'target': rng.choice([0, 1], size=n_rows, p=[0.7, 0.3])
    }
    
    res = pd.DataFrame(data)
    
    logger.info(
        'Первичный синтетический DataFrame создан. '
        f'Размер: {res.shape}, '
        f'Количество пропусков в account_balance: {res['account_balance'].isna().sum()}'
    )
    
    return res

# Примитивно написанный код с использованием только NumPy и Pandas
'''
raw_df = generate_data(100_000)
print(f"Размер датасета: {raw_df.shape}")
print(f"Количество пропусков в account_balance: {raw_df['account_balance'].isna().sum()}")

# Перемешиваем индексы датасета для случайного сплита
rng = np.random.default_rng(seed=42)

shuffled_indices = rng.permutation(len(raw_df))
train_size = int(len(raw_df) * 0.8)

train_idx = shuffled_indices[:train_size]
test_idx = shuffled_indices[train_size:]

train_clean = raw_df.iloc[train_idx].copy()
test_clean = raw_df.iloc[test_idx].copy()


train_balance_mean = train_clean['account_balance'].mean()
train_target_map = train_clean.groupby("user_group")['target'].mean().to_dict()
global_target_mean = train_clean['target'].mean()

train_clean['account_balance'] = train_clean['account_balance'].fillna(train_balance_mean)
train_clean['user_group_encoded'] = (train_clean['user_group']
                                     .map(train_target_map)
                                     .fillna(global_target_mean)
                                     )
train_clean = train_clean.drop(columns=['user_group'])
'''



class ProductionDataPreprocessor:
    '''
    Трансформер данных, гарантирующий полное отсутствие Data Leakage.

    Выполняет импутацию пропусков и Target Encoding строго на основе
    статистик, посчитанных на этапе fit().
    '''
    
    def __init__(
        self,
        numeric_col: str,
        categorical_col: str,
        target_col: str,
    ) -> None:
        
        self.numeric_col = numeric_col
        self.categorical_col = categorical_col
        self.target_col = target_col
        
        self.balance_mean_: Optional[float] = None
        self.target_map_: Dict[str, float] = {}
        self.global_target_mean_: Optional[float] = None
        self.is_fitted_: bool = False
    
    def fit(self, df: pd.DataFrame) -> 'ProductionDataPreprocessor':
        '''Вычисляет и фиксирует все необходимые статистики по обучающему DataFrame.'''
        
        logger.info(
            'Старт вычисления статистик (fit) на обучающей выборке...'
        )
        
        self.balance_mean_ = float(df[self.numeric_col].mean())
        self.global_target_mean_ = float(df[self.target_col].mean())
        self.target_map_ = (
            df.groupby(self.categorical_col)[
                self.target_col
            ].mean().to_dict()
        )
        
        self.is_fitted_ = True
        
        logger.info(
            f'Fit завершен. Средний баланс: {self.balance_mean_:.2f}, ' 
            f'Категорий закодировано: {len(self.target_map_)}'
        )
        
        return self
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        Применяет зафиксированные ранее статистики к переданному DataFrame.
        '''
        
        if not self.is_fitted_:
            raise RuntimeError(
                'Трансформер еще не обучен! Сначала вызовите метод .fit()'
            )
        
        logger.info(
            'Применение трансформаций (transform)...'
        )
        
        df_transformed = df.copy()
        
        df_transformed[self.numeric_col] = (
            df_transformed[self.numeric_col]
            .fillna(self.balance_mean_)
            )
        
        df_transformed[f'{self.categorical_col}_encoded'] = (
            df_transformed[self.categorical_col]
            .map(self.target_map_)
            .fillna(self.global_target_mean_)
            )
        
        df_transformed = df_transformed.drop(columns=[self.categorical_col])
        
        return df_transformed
    
    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        Удобный совмещенный метод для обучающей выборки (последовательный вызов .fit() и .transform()).
        '''
        
        return self.fit(df).transform(df)


def main() -> None:
    'Точка входа для эмуляции ML-пайплайна подготовки данных.'
    
    logger.info(
        'Запуск основного пайплайна...'
    )
    
    raw_df = generate_data(100_000)
    
    train_df, test_df = train_test_split(raw_df, test_size=0.2, random_state=42)
    
    preprocessor = ProductionDataPreprocessor(
        numeric_col='account_balance',
        categorical_col='user_group',
        target_col='target',
    )
    
    train_processed = preprocessor.fit_transform(train_df)
    test_processed = preprocessor.transform(test_df)
    
    logger.info('Готовый Train DataFrame (первые 3 строки):\n%s', train_processed.head(3))
    logger.info('Готовый Test DataFrame (первые 3 строки):\n%s', test_processed.head(3))

if __name__ == '__main__':
    main()