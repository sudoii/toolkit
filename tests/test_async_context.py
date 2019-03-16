import pytest

from toolkit.async_context import contextmanager


class TestError(RuntimeError):
    pass


@contextmanager
def sync_method():
    yield 1


@contextmanager
def sync_method_error_before():
    raise TestError()
    yield 1


@contextmanager
def sync_method_error_after():
    yield 1
    raise TestError()


@contextmanager
async def async_method():
    yield 2


@contextmanager
async def async_method_error_before():
    raise TestError()
    yield 2


@contextmanager
async def async_method_error_after():
    yield 2
    raise TestError()


class TestContextManager(object):

    def test_sync_method_with_sync(self):
        with sync_method() as rs:
            assert rs == 1

    def test_sync_method_with_sync_with_error(self):
        with pytest.raises(TestError):
            with sync_method() as rs:
                assert rs == 1
                raise TestError()

    def test_sync_method_with_sync_with_inner_error_before(self):
        with pytest.raises(TestError):
            with sync_method_error_before() as rs:
                pass

    def test_sync_method_with_sync_with_inner_error_after(self):
        with pytest.raises(TestError):
            with sync_method_error_after() as rs:
                assert rs == 1

    @pytest.mark.asyncio
    async def test_sync_method_with_async(self):
        async with sync_method() as rs:
            assert rs == 1

    @pytest.mark.asyncio
    async def test_sync_method_with_async_with_error(self):
        with pytest.raises(TestError):
            async with sync_method() as rs:
                assert rs == 1
                raise TestError()

    @pytest.mark.asyncio
    async def test_sync_method_with_async_with_inner_error_before(self):
        with pytest.raises(TestError):
            async with sync_method_error_before() as rs:
                pass

    @pytest.mark.asyncio
    async def test_sync_method_with_async_with_inner_error_after(self):
        with pytest.raises(TestError):
            async with sync_method_error_after() as rs:
                assert rs == 1

    @pytest.mark.asyncio
    async def test_async_method_with_async(self):
        async with async_method() as rs:
            assert rs == 2

    @pytest.mark.asyncio
    async def test_async_method_with_async_with_error(self):
        with pytest.raises(TestError):
            async with async_method() as rs:
                assert rs == 2
                raise TestError("111")

    @pytest.mark.asyncio
    async def test_async_method_with_async_with_inner_error_before(self):
        with pytest.raises(TestError):
            async with async_method_error_before() as rs:
                pass

    @pytest.mark.asyncio
    async def test_async_method_with_async_with_inner_error_after(self):
        with pytest.raises(TestError):
            async with async_method_error_after() as rs:
                assert rs == 2

    @pytest.mark.asyncio
    async def test_async_method_with_sync(self):
        with async_method() as rs:
            assert rs == 2

    @pytest.mark.asyncio
    async def test_async_method_with_sync_with_error(self):
        with pytest.raises(TestError):
            with async_method() as rs:
                assert rs == 2
                raise TestError("111")

    @pytest.mark.asyncio
    async def test_async_method_with_sync_with_inner_error_before(self):
        with pytest.raises(TestError):
            with async_method_error_before() as rs:
                pass

    @pytest.mark.asyncio
    async def test_async_method_with_sync_with_inner_error_after(self):
        with pytest.raises(TestError):
            with async_method_error_after() as rs:
                assert rs == 2