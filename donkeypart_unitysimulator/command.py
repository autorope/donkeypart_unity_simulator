import socketio
import argparse

class Sim():
    """
    Start a websocket SocketIO server to talk to a donkey simulator
    """

    def parse_args(self, args):
        parser = argparse.ArgumentParser(prog='sim')
        parser.add_argument('--model', help='the model to use for predictions')
        parser.add_argument('--config', default='./config.py', help='location of config file to use. default: ./config.py')
        parser.add_argument('--type', default='categorical', help='model type to use when loading. categorical|linear')
        parser.add_argument('--top_speed', default='3', help='what is top speed to drive')
        parsed_args = parser.parse_args(args)
        return parsed_args, parser

    def run(self, args):
        '''
        Start a websocket SocketIO server to talk to a donkey simulator
        '''


        args, parser = self.parse_args(args)

        if cfg is None:
            return

        #TODO: this logic should be in a pilot or modle handler part.
        if args.type == "categorical":
            kl = KerasCategorical()
        elif args.type == "linear":
            kl = KerasLinear(num_outputs=2)
        else:
            print("didn't recognice type:", args.type)
            return

        #can provide an optional image filter part
        img_stack = None


        #start sim server handler
        ss = SteeringServer(sio, top_speed=top_speed, image_part=img_stack)


