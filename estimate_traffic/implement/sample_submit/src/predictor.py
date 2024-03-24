import pandas as pd
import pickle
import tqdm
from sklearn.preprocessing import LabelEncoder
import os

class ScoringService(object):
    @classmethod
    def get_model(cls, model_path, inference_df, inference_log):
        """Get model method

        Args:
            model_path (str): Path to the trained model directory.
            inference_df: Past data not subject to prediction.
            inference_log: Past log data that is not subject to prediction.

        Returns:
            bool: The return value. True for success.
        """
        model_path = os.path.join(model_path,"trained_model.pkl"))

        # カレントディレクトリにあるモデルデータの読み込み
        gbm = pickle.load(open(model_path, 'rb'))
        print("gbm type:::{}".format(type(gbm)))
        print("gbm:::{}".format(gbm))

        prediction = cls.label_encode(inference_df)

        cls.model = gbm[0]
        cls.data = prediction
        cls.log_paths = inference_log

        return cls.model, cls.data, cls.log_paths


    @classmethod
    def predict(cls,model, data, log_paths, input, input_log):
        """Predict method

        Args:
            input: meta data of the sample you want to make inference from (DataFrame)
            input_log: meta data of the sample you want to make inference from (DataFrame)

        Returns:
            prediction: Inference for the given input. Return columns must be ['datetime', 'start_code', 'end_code', 'KP'](DataFrame).
        """
        # prediction = data.copy()
        # prediction['weekday'] = pd.to_datetime(prediction['datetime'], format='%Y-%m-%d').apply(lambda x: x.weekday())
        # prediction['prediction'] = prediction['weekday'].apply(lambda x: 1 if x==4 or x==5 else 0)
        result = data.copy()
        
        cat_cols = ['road_code', 'start_code', 'end_code', 'section', 'direction', 'hour', 'dayofweek']
        num_cols = ['year', 'month', 'day', 'search_specified', 'search_unspecified', 'KP', 'start_KP', 'end_KP', 'limit_speed']
        feature_cols = cat_cols + num_cols
        # 学習用特長量
        prediction = data[feature_cols]
        print(prediction)
        # 推論結果
        predict = model.predict(prediction)

        # print("prpedict result {}".format(pd.DataFrame(predict).describe()))

        # 推論結果を元データへ追加
        result['prediction'] = predict

        # 提出データを作成
        submit_data = result[['datetime', 'start_code', 'end_code', 'KP', 'prediction']]
        return submit_data, pd.DataFrame(predict)

    def label_encode(data):
        cat_cols = ['road_code', 'start_code', 'end_code', 'section', 'direction', 'hour', 'dayofweek']
        # ========================================
        # カテゴリ変数の処理
        # ========================================
        le_dict = {}
        for c in cat_cols:
            le = LabelEncoder()
            # print(data[c])
            data[c] = le.fit_transform(data[c])
            le_dict[c] = le
        return data