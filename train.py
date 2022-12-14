import argparse
import core

def ArgumentParser():
    parser = argparse.ArgumentParser(description='n-граммная языковая модель')
    parser.add_argument('--input-dir', type=str, 
                        help='путь к директории, в которой лежит коллекция документов. Если данный аргумент не задан, считать, что тексты вводятся из stdin.')
    parser.add_argument('--model', type=str,
                        help='путь к файлу, в который сохраняется модель.')
    return parser

def train(input_dir, model_path):
    model = core.model(texts_path=input_dir, path=model_path)
    model.fit()

if __name__ == "__main__":
    args = ArgumentParser().parse_args()
    train(args.input_dir, args.model)