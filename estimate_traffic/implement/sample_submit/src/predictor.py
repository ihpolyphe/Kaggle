import pandas as pd
import pickle

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

        # カレントディレクトリにあるモデルデータの読み込み
        gbm = pickle.load(open(model_path, 'rb'))


        cls.model = gbm[0]
        cls.data = inference_df
        cls.log_pathes = inference_log

        return True


    @classmethod
    def predict(cls, input, input_log):
        """Predict method

        Args:
            input: meta data of the sample you want to make inference from (DataFrame)
            input_log: meta data of the sample you want to make inference from (DataFrame)

        Returns:
            prediction: Inference for the given input. Return columns must be ['datetime', 'start_code', 'end_code', 'KP'](DataFrame).
        """
        print("input {}".format(input.info()))
        print("input_log {}".format(input_log.info()))
        prediction = input.copy()
        prediction['weekday'] = pd.to_datetime(prediction['datetime'], format='%Y-%m-%d').apply(lambda x: x.weekday())
        prediction['prediction'] = prediction['weekday'].apply(lambda x: 1 if x==4 or x==5 else 0)
        predict = cls.model.predict(prediction)
        print(predict)
        prediction = prediction[['datetime', 'start_code', 'end_code', 'KP', 'prediction']]

        return prediction
