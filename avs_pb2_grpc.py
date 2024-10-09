# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import avs_pb2 as avs__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


class AggregatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetKey = channel.unary_unary(
                '/aggregator.Aggregator/GetKey',
                request_serializer=avs__pb2.GetKeyReq.SerializeToString,
                response_deserializer=avs__pb2.KeyResp.FromString,
                _registered_method=True)
        self.GetNonce = channel.unary_unary(
                '/aggregator.Aggregator/GetNonce',
                request_serializer=avs__pb2.NonceRequest.SerializeToString,
                response_deserializer=avs__pb2.NonceResp.FromString,
                _registered_method=True)
        self.GetSmartAccountAddress = channel.unary_unary(
                '/aggregator.Aggregator/GetSmartAccountAddress',
                request_serializer=avs__pb2.AddressRequest.SerializeToString,
                response_deserializer=avs__pb2.AddressResp.FromString,
                _registered_method=True)
        self.CreateTask = channel.unary_unary(
                '/aggregator.Aggregator/CreateTask',
                request_serializer=avs__pb2.CreateTaskReq.SerializeToString,
                response_deserializer=avs__pb2.CreateTaskResp.FromString,
                _registered_method=True)
        self.ListTasks = channel.unary_unary(
                '/aggregator.Aggregator/ListTasks',
                request_serializer=avs__pb2.ListTasksReq.SerializeToString,
                response_deserializer=avs__pb2.ListTasksResp.FromString,
                _registered_method=True)
        self.GetTask = channel.unary_unary(
                '/aggregator.Aggregator/GetTask',
                request_serializer=avs__pb2.UUID.SerializeToString,
                response_deserializer=avs__pb2.Task.FromString,
                _registered_method=True)
        self.CancelTask = channel.unary_unary(
                '/aggregator.Aggregator/CancelTask',
                request_serializer=avs__pb2.UUID.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.FromString,
                _registered_method=True)
        self.DeleteTask = channel.unary_unary(
                '/aggregator.Aggregator/DeleteTask',
                request_serializer=avs__pb2.UUID.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.FromString,
                _registered_method=True)
        self.Ping = channel.unary_unary(
                '/aggregator.Aggregator/Ping',
                request_serializer=avs__pb2.Checkin.SerializeToString,
                response_deserializer=avs__pb2.CheckinResp.FromString,
                _registered_method=True)
        self.SyncTasks = channel.unary_stream(
                '/aggregator.Aggregator/SyncTasks',
                request_serializer=avs__pb2.SyncTasksReq.SerializeToString,
                response_deserializer=avs__pb2.SyncTasksResp.FromString,
                _registered_method=True)
        self.UpdateChecks = channel.unary_unary(
                '/aggregator.Aggregator/UpdateChecks',
                request_serializer=avs__pb2.UpdateChecksReq.SerializeToString,
                response_deserializer=avs__pb2.UpdateChecksResp.FromString,
                _registered_method=True)


class AggregatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetKey(self, request, context):
        """Auth
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNonce(self, request, context):
        """Smart Acccount
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSmartAccountAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTask(self, request, context):
        """Task Management
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ping(self, request, context):
        """Operator endpoint
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SyncTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateChecks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AggregatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GetKey,
                    request_deserializer=avs__pb2.GetKeyReq.FromString,
                    response_serializer=avs__pb2.KeyResp.SerializeToString,
            ),
            'GetNonce': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNonce,
                    request_deserializer=avs__pb2.NonceRequest.FromString,
                    response_serializer=avs__pb2.NonceResp.SerializeToString,
            ),
            'GetSmartAccountAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSmartAccountAddress,
                    request_deserializer=avs__pb2.AddressRequest.FromString,
                    response_serializer=avs__pb2.AddressResp.SerializeToString,
            ),
            'CreateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTask,
                    request_deserializer=avs__pb2.CreateTaskReq.FromString,
                    response_serializer=avs__pb2.CreateTaskResp.SerializeToString,
            ),
            'ListTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTasks,
                    request_deserializer=avs__pb2.ListTasksReq.FromString,
                    response_serializer=avs__pb2.ListTasksResp.SerializeToString,
            ),
            'GetTask': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTask,
                    request_deserializer=avs__pb2.UUID.FromString,
                    response_serializer=avs__pb2.Task.SerializeToString,
            ),
            'CancelTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelTask,
                    request_deserializer=avs__pb2.UUID.FromString,
                    response_serializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.SerializeToString,
            ),
            'DeleteTask': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTask,
                    request_deserializer=avs__pb2.UUID.FromString,
                    response_serializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.SerializeToString,
            ),
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=avs__pb2.Checkin.FromString,
                    response_serializer=avs__pb2.CheckinResp.SerializeToString,
            ),
            'SyncTasks': grpc.unary_stream_rpc_method_handler(
                    servicer.SyncTasks,
                    request_deserializer=avs__pb2.SyncTasksReq.FromString,
                    response_serializer=avs__pb2.SyncTasksResp.SerializeToString,
            ),
            'UpdateChecks': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateChecks,
                    request_deserializer=avs__pb2.UpdateChecksReq.FromString,
                    response_serializer=avs__pb2.UpdateChecksResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aggregator.Aggregator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('aggregator.Aggregator', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Aggregator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aggregator.Aggregator/GetKey',
            avs__pb2.GetKeyReq.SerializeToString,
            avs__pb2.KeyResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetNonce(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aggregator.Aggregator/GetNonce',
            avs__pb2.NonceRequest.SerializeToString,
            avs__pb2.NonceResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetSmartAccountAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aggregator.Aggregator/GetSmartAccountAddress',
            avs__pb2.AddressRequest.SerializeToString,
            avs__pb2.AddressResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aggregator.Aggregator/CreateTask',
            avs__pb2.CreateTaskReq.SerializeToString,
            avs__pb2.CreateTaskResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aggregator.Aggregator/ListTasks',
            avs__pb2.ListTasksReq.SerializeToString,
            avs__pb2.ListTasksResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aggregator.Aggregator/GetTask',
            avs__pb2.UUID.SerializeToString,
            avs__pb2.Task.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CancelTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aggregator.Aggregator/CancelTask',
            avs__pb2.UUID.SerializeToString,
            google_dot_protobuf_dot_wrappers__pb2.BoolValue.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aggregator.Aggregator/DeleteTask',
            avs__pb2.UUID.SerializeToString,
            google_dot_protobuf_dot_wrappers__pb2.BoolValue.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aggregator.Aggregator/Ping',
            avs__pb2.Checkin.SerializeToString,
            avs__pb2.CheckinResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SyncTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/aggregator.Aggregator/SyncTasks',
            avs__pb2.SyncTasksReq.SerializeToString,
            avs__pb2.SyncTasksResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateChecks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aggregator.Aggregator/UpdateChecks',
            avs__pb2.UpdateChecksReq.SerializeToString,
            avs__pb2.UpdateChecksResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
